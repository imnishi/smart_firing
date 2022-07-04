// Generated by gencpp from file hector_nav_msgs/GetNormalResponse.msg
// DO NOT EDIT!


#ifndef HECTOR_NAV_MSGS_MESSAGE_GETNORMALRESPONSE_H
#define HECTOR_NAV_MSGS_MESSAGE_GETNORMALRESPONSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <geometry_msgs/Vector3.h>

namespace hector_nav_msgs
{
template <class ContainerAllocator>
struct GetNormalResponse_
{
  typedef GetNormalResponse_<ContainerAllocator> Type;

  GetNormalResponse_()
    : normal()  {
    }
  GetNormalResponse_(const ContainerAllocator& _alloc)
    : normal(_alloc)  {
  (void)_alloc;
    }



   typedef  ::geometry_msgs::Vector3_<ContainerAllocator>  _normal_type;
  _normal_type normal;





  typedef boost::shared_ptr< ::hector_nav_msgs::GetNormalResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::hector_nav_msgs::GetNormalResponse_<ContainerAllocator> const> ConstPtr;

}; // struct GetNormalResponse_

typedef ::hector_nav_msgs::GetNormalResponse_<std::allocator<void> > GetNormalResponse;

typedef boost::shared_ptr< ::hector_nav_msgs::GetNormalResponse > GetNormalResponsePtr;
typedef boost::shared_ptr< ::hector_nav_msgs::GetNormalResponse const> GetNormalResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::hector_nav_msgs::GetNormalResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::hector_nav_msgs::GetNormalResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::hector_nav_msgs::GetNormalResponse_<ContainerAllocator1> & lhs, const ::hector_nav_msgs::GetNormalResponse_<ContainerAllocator2> & rhs)
{
  return lhs.normal == rhs.normal;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::hector_nav_msgs::GetNormalResponse_<ContainerAllocator1> & lhs, const ::hector_nav_msgs::GetNormalResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace hector_nav_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::hector_nav_msgs::GetNormalResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::hector_nav_msgs::GetNormalResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::hector_nav_msgs::GetNormalResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::hector_nav_msgs::GetNormalResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::hector_nav_msgs::GetNormalResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::hector_nav_msgs::GetNormalResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::hector_nav_msgs::GetNormalResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "9a5880458dbcd28bf7ed1889c8ac7f8e";
  }

  static const char* value(const ::hector_nav_msgs::GetNormalResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x9a5880458dbcd28bULL;
  static const uint64_t static_value2 = 0xf7ed1889c8ac7f8eULL;
};

template<class ContainerAllocator>
struct DataType< ::hector_nav_msgs::GetNormalResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "hector_nav_msgs/GetNormalResponse";
  }

  static const char* value(const ::hector_nav_msgs::GetNormalResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::hector_nav_msgs::GetNormalResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "geometry_msgs/Vector3 normal\n"
"\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Vector3\n"
"# This represents a vector in free space. \n"
"# It is only meant to represent a direction. Therefore, it does not\n"
"# make sense to apply a translation to it (e.g., when applying a \n"
"# generic rigid transformation to a Vector3, tf2 will only apply the\n"
"# rotation). If you want your data to be translatable too, use the\n"
"# geometry_msgs/Point message instead.\n"
"\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
;
  }

  static const char* value(const ::hector_nav_msgs::GetNormalResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::hector_nav_msgs::GetNormalResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.normal);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct GetNormalResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::hector_nav_msgs::GetNormalResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::hector_nav_msgs::GetNormalResponse_<ContainerAllocator>& v)
  {
    s << indent << "normal: ";
    s << std::endl;
    Printer< ::geometry_msgs::Vector3_<ContainerAllocator> >::stream(s, indent + "  ", v.normal);
  }
};

} // namespace message_operations
} // namespace ros

#endif // HECTOR_NAV_MSGS_MESSAGE_GETNORMALRESPONSE_H
