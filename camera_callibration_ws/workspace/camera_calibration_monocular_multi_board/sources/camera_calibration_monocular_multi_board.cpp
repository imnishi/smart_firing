/*
 * Written by: Ashish Kumar
 * Ph.D. EE
 * IIT Kanpur, India
 * 05-08-2021
 *
*/

#include<stdio.h>
#include <iostream>
#include<vector>

#include <opencv2/opencv.hpp>

#include<boost/filesystem.hpp>

void detect_points(int n_boards,
                   std::vector<bool>& skip_board,
                   std::vector<cv::Size>& board_sizes,
                   std::vector<float>& board_square_dims,
                   cv::Size& image_size,
                   std::vector<std::vector<std::string> >& str_all_left_images,
                   std::vector<std::vector<cv::Point3f> >& world_points,
                   std::vector<std::vector<cv::Point2f> >& left_image_points);


void save_images(int n_boards,
                 std::vector<bool>& skip_board,
                 int max_imgs_per_board,
                 std::vector<cv::Size>& board_sizes,
                 cv::Size& image_size,
                 std::string& str_image_dir);


int main(int argc, char** argv)
{
    std::cout << "Syntax: " + std::string(argv[0]) + " capture_images " + " calibrate \n";
    std::cout << "Usage: " + std::string(argv[0]) + " 1/0 " + " 1/0 \n\n";

    if(argc <3)
    {
        std::cout << "Please specify desired number of arguments\n";
        return 1;
    }

    int  capture_images = std::atoi(argv[1]);
    int  calibrate = std::atoi(argv[2]);

    int n_boards = 4;
    int max_imgs_per_board = 50;

//        cv::Size save_image_size(1920, 1080);
//    cv::Size save_image_size(320, 240);
    //cv::Size save_image_size(640, 480);
    cv::Size save_image_size(800,600);

    //    cv::Size calibrate_image_size(1280, 720);
    //        cv::Size calibrate_image_size(1280, 720);
    //cv::Size calibrate_image_size(640, 480);
//    cv::Size calibrate_image_size(1920, 1080);
	cv::Size calibrate_image_size(800,600);

    std::vector<int> board_height(n_boards);
    std::vector<int> board_width(n_boards);
    std::vector<float> board_square_dims(n_boards);

    std::vector<bool> skip_board(n_boards);

    // inner corners
    int board_idx = 0;
    board_height[board_idx] = 8;
    board_width[board_idx] = 6;
    board_square_dims[board_idx] = 0.030;
    skip_board[board_idx] = false;
    board_idx++;

    board_height[board_idx] = 11;
    board_width[board_idx] = 7;
    board_square_dims[board_idx] = 0.050;
    skip_board[board_idx] = true;
    board_idx++;

    board_height[board_idx] = 9;
    board_width[board_idx] = 5;
    board_square_dims[board_idx] = 0.060;
    skip_board[board_idx] = true;
    board_idx++;

    board_height[board_idx] = 6;
    board_width[board_idx] = 4;
    board_square_dims[board_idx] = 0.080;
    skip_board[board_idx] = true;
    board_idx++;

    //board 4 is best performing



    std::vector<cv::Size> board_sizes(n_boards);

    for(int i=0;i<n_boards;i++)
    {
        board_sizes[i].width = board_width[i];
        board_sizes[i].height = board_height[i];
    }


    bool is_elp_rig = false;


    std::string str_calib_dir = "/home/isl-server/monocular/";
    std::string str_image_dir = str_calib_dir + "checkerboard_images/board_";

    std::stringstream calib_file;
    calib_file << calibrate_image_size.width << "x" << calibrate_image_size.height;

    std::string str_cam_parameters_file =  str_calib_dir + "camera_parameters_" + calib_file.str() + ".txt";


    // save_images
    if(capture_images)
    {
            save_images(n_boards,
                        skip_board,
                        max_imgs_per_board,
                        board_sizes, save_image_size,
                        str_image_dir);
    }

    if(calibrate)
    {

        std::vector<std::vector<std::string> > str_all_left_images(n_boards);

        // Get images paths
        for(int i=0;i<n_boards;i++)
        {
            if(skip_board[i])
                continue;

            std::stringstream str_board_id;
            str_board_id << i;

            std::vector<std::string>& str_left_images = str_all_left_images[i];

            {
                std::string str_cam_dir = str_image_dir + str_board_id.str() + "/left/";

                boost::filesystem::directory_iterator dir_iterator(str_cam_dir);

                std::vector<std::string> str_all_images;

                while( dir_iterator != boost::filesystem::directory_iterator())
                {
                    str_all_images.push_back((*dir_iterator).path().filename().string());
                    *dir_iterator++;
                }

                std::sort(str_all_images.begin(), str_all_images.end());

                int max_ims = str_all_images.size();
                for(int j = 0; j < max_ims; j++)
                    str_left_images.push_back(str_cam_dir + str_all_images[j]);
            }
        }


        std::vector<std::vector<cv::Point3f> > world_points;
        std::vector<std::vector<cv::Point2f> > left_image_points;

        std::cout << "POPULATING CORNERS FOR THE CAMERA\n";
        detect_points(n_boards, skip_board,
                      board_sizes, board_square_dims,
                      calibrate_image_size,
                      str_all_left_images,
                      world_points, left_image_points);


        cv::Mat K_left;
        cv::Mat D_left;
        std::vector<cv::Mat> Rs_left;
        std::vector<cv::Mat> Ts_left;


        std::cout << "CALIBRATING left CAM\n";
        cv::calibrateCamera(world_points, left_image_points, calibrate_image_size,
                            K_left, D_left, Rs_left, Ts_left,
                            CV_CALIB_FIX_PRINCIPAL_POINT);// CV_CALIB_FIX_K4 | CV_CALIB_FIX_K5);

        float left_error = 0;

        for(int i=0;i<world_points.size();i++)
        {
            std::vector<cv::Point2f> proj_left_image_points;

            cv::projectPoints(world_points[i], Rs_left[i], Ts_left[i], K_left, D_left, proj_left_image_points);

            std::vector<cv::Point2f>& left_points = left_image_points[i];

            for(int j=0;j<left_points.size();j++)
            {
                cv::Point2f& l_pt = left_points[j];
                cv::Point2f& proj_l_pt = proj_left_image_points[j];

                left_error += sqrt((l_pt.x - proj_l_pt.x)*(l_pt.x - proj_l_pt.x) + (l_pt.y - proj_l_pt.y)*(l_pt.y - proj_l_pt.y));
            }
        }

        std::cout << "l error = " << left_error/ world_points.size() << "\n";

        std::cout << K_left << "\n";
        std::cout << D_left << "\n";

        cv::FileStorage fs(str_cam_parameters_file.c_str(), cv::FileStorage::WRITE);

        fs << "K_left" << K_left;
        fs << "D_left" <<  D_left;

        fs.release();
    }

    return 0;
}


void save_images(int n_boards,
                 std::vector<bool>& skip_board,
                 int max_imgs_per_board,
                 std::vector<cv::Size>& board_sizes,
                 cv::Size& image_size,
                 std::string& str_image_dir)
{
    for(int i=0; i<n_boards;i++)
    {
        if(skip_board[i])
            continue;

        std::stringstream board_idx;
        board_idx << i;

        boost::filesystem::create_directories(str_image_dir + board_idx.str() + "/left");
    }

    cv::VideoCapture capl(0);

    std::cout << image_size << "\n";

    capl.set(CV_CAP_PROP_FRAME_HEIGHT, image_size.height);
    capl.set(CV_CAP_PROP_FRAME_WIDTH, image_size.width);

    capl.set(CV_CAP_PROP_FOURCC, CV_FOURCC('M','J','P','G'));

    for(int i=0; i<n_boards;i++)
    {
        if(skip_board[i])
            continue;

        cv::Size& board_size = board_sizes[i];

        std::stringstream board_idx;
        board_idx << i;

        std::string str_board_dir = str_image_dir + board_idx.str();

        int n_images = 0;
        while(n_images < max_imgs_per_board)
        {
            cv::Mat left_image;

            capl.grab();

            capl >> left_image;

            cv::Mat corner_left_image;

            left_image.copyTo(corner_left_image);

            cv::cvtColor(left_image, left_image, CV_BGR2GRAY);

            std::vector<cv::Point2f> left_corners;

            bool found_corners = false;


            found_corners = cv::findChessboardCorners(left_image,
                                                      board_size,
                                                      left_corners,
                                                      CV_CALIB_CB_ADAPTIVE_THRESH + CV_CALIB_CB_FILTER_QUADS);

            cv::drawChessboardCorners(corner_left_image, board_size, left_corners, found_corners);

            //resize for visualization
            cv::resize(corner_left_image, corner_left_image, cv::Size(800,600));

            cv::imshow("left corners", corner_left_image);
            unsigned char key = cv::waitKey(1);

            if(found_corners && key == 32)
            {
                std::stringstream im_idx;
                im_idx << n_images;

                cv::imwrite(str_board_dir + "/left/" + im_idx.str() + ".png", left_image);
                n_images++;

                std::cout << "Written " << n_images << " images for board " << board_idx.str() << "\n";
            }

            if(n_images == max_imgs_per_board)
            {
                if(i < n_boards-1)
                {
                    std::cout << "Please change the board and press any key on the image \n";
                    std::cout << "Next board size = " << board_sizes[i+1].height << "*" << board_sizes[i+1].width <<  "\n";
                }
            }
        }
    }
}



void detect_points(int n_boards,
                   std::vector<bool>& skip_board,
                   std::vector<cv::Size>& board_sizes,
                   std::vector<float>& board_square_dims,
                   cv::Size& image_size,
                   std::vector<std::vector<std::string> >& str_all_left_images,
                   std::vector<std::vector<cv::Point3f> >& world_points,
                   std::vector<std::vector<cv::Point2f> >& left_image_points)
{

    for(int board_idx = 0; board_idx < n_boards; board_idx++)
    {
        if(skip_board[board_idx])
            continue;

        cv::Size& board_size = board_sizes[board_idx];

        int board_height = board_size.height;
        int board_width = board_size.width;
        float board_square_dim = board_square_dims[board_idx];

        std::vector<cv::Point3f> board_points;

        for(int j = 0;j<board_height; j++)
            for(int k = 0;k<board_width;k++)
                board_points.push_back(cv::Point3f((float)k * board_square_dim, (float)j * board_square_dim, 0));

        std::vector<std::string>& str_left_images = str_all_left_images[board_idx];

        int n_images = str_left_images.size();

        for(int i=0;i<n_images;i++)
        {
            std::string& left_image_name = str_left_images[i];

            std::cout  << left_image_name << " \n";

            cv::Mat left_image = cv::imread(left_image_name);

            cv::resize(left_image, left_image, image_size);

            cv::Mat corner_left_image;

            left_image.copyTo(corner_left_image);

            cv::cvtColor(left_image, left_image, CV_BGR2GRAY);

            std::vector<cv::Point2f> left_corners;

            bool found_corners = false;

            found_corners = cv::findChessboardCorners(left_image,
                                                      board_size,
                                                      left_corners,
                                                      CV_CALIB_CB_ADAPTIVE_THRESH | CV_CALIB_CB_FILTER_QUADS | CV_CALIB_CB_FAST_CHECK);


            if (found_corners)
            {
                std::cout << "Calib Board_idx = " << board_idx << ", Corners Found in image " << i << std::endl;

                cv::cornerSubPix(left_image,
                                 left_corners,
                                 cv::Size(5, 5),
                                 cv::Size(-1, -1),
                                 cv::TermCriteria(CV_TERMCRIT_EPS | CV_TERMCRIT_ITER, 30, 0.1));

                cv::drawChessboardCorners(corner_left_image,board_size,left_corners,found_corners);

                //resize for visualization
                cv::resize(corner_left_image, corner_left_image, cv::Size(800,600));

                cv::imshow("left corners", corner_left_image);
                cv::waitKey(1);

                left_image_points.push_back(left_corners);
                world_points.push_back(board_points);
            }
        }
    }
}

