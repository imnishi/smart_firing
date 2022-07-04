// Generated by gencpp from file roborts_msgs/RobotStatus.msg
// DO NOT EDIT!


#ifndef ROBORTS_MSGS_MESSAGE_ROBOTSTATUS_H
#define ROBORTS_MSGS_MESSAGE_ROBOTSTATUS_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace roborts_msgs
{
template <class ContainerAllocator>
struct RobotStatus_
{
  typedef RobotStatus_<ContainerAllocator> Type;

  RobotStatus_()
    : id(0)
    , level(0)
    , remain_hp(0)
    , max_hp(0)
    , heat_cooling_limit(0)
    , heat_cooling_rate(0)
    , gimbal_output(false)
    , chassis_output(false)
    , shooter_output(false)  {
    }
  RobotStatus_(const ContainerAllocator& _alloc)
    : id(0)
    , level(0)
    , remain_hp(0)
    , max_hp(0)
    , heat_cooling_limit(0)
    , heat_cooling_rate(0)
    , gimbal_output(false)
    , chassis_output(false)
    , shooter_output(false)  {
  (void)_alloc;
    }



   typedef uint8_t _id_type;
  _id_type id;

   typedef uint8_t _level_type;
  _level_type level;

   typedef uint16_t _remain_hp_type;
  _remain_hp_type remain_hp;

   typedef uint16_t _max_hp_type;
  _max_hp_type max_hp;

   typedef uint16_t _heat_cooling_limit_type;
  _heat_cooling_limit_type heat_cooling_limit;

   typedef uint16_t _heat_cooling_rate_type;
  _heat_cooling_rate_type heat_cooling_rate;

   typedef uint8_t _gimbal_output_type;
  _gimbal_output_type gimbal_output;

   typedef uint8_t _chassis_output_type;
  _chassis_output_type chassis_output;

   typedef uint8_t _shooter_output_type;
  _shooter_output_type shooter_output;





  typedef boost::shared_ptr< ::roborts_msgs::RobotStatus_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::roborts_msgs::RobotStatus_<ContainerAllocator> const> ConstPtr;

}; // struct RobotStatus_

typedef ::roborts_msgs::RobotStatus_<std::allocator<void> > RobotStatus;

typedef boost::shared_ptr< ::roborts_msgs::RobotStatus > RobotStatusPtr;
typedef boost::shared_ptr< ::roborts_msgs::RobotStatus const> RobotStatusConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::roborts_msgs::RobotStatus_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::roborts_msgs::RobotStatus_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::roborts_msgs::RobotStatus_<ContainerAllocator1> & lhs, const ::roborts_msgs::RobotStatus_<ContainerAllocator2> & rhs)
{
  return lhs.id == rhs.id &&
    lhs.level == rhs.level &&
    lhs.remain_hp == rhs.remain_hp &&
    lhs.max_hp == rhs.max_hp &&
    lhs.heat_cooling_limit == rhs.heat_cooling_limit &&
    lhs.heat_cooling_rate == rhs.heat_cooling_rate &&
    lhs.gimbal_output == rhs.gimbal_output &&
    lhs.chassis_output == rhs.chassis_output &&
    lhs.shooter_output == rhs.shooter_output;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::roborts_msgs::RobotStatus_<ContainerAllocator1> & lhs, const ::roborts_msgs::RobotStatus_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace roborts_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::roborts_msgs::RobotStatus_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::roborts_msgs::RobotStatus_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::roborts_msgs::RobotStatus_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::roborts_msgs::RobotStatus_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::roborts_msgs::RobotStatus_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::roborts_msgs::RobotStatus_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::roborts_msgs::RobotStatus_<ContainerAllocator> >
{
  static const char* value()
  {
    return "122334534857c1294574d2c7eef57af5";
  }

  static const char* value(const ::roborts_msgs::RobotStatus_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x122334534857c129ULL;
  static const uint64_t static_value2 = 0x4574d2c7eef57af5ULL;
};

template<class ContainerAllocator>
struct DataType< ::roborts_msgs::RobotStatus_<ContainerAllocator> >
{
  static const char* value()
  {
    return "roborts_msgs/RobotStatus";
  }

  static const char* value(const ::roborts_msgs::RobotStatus_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::roborts_msgs::RobotStatus_<ContainerAllocator> >
{
  static const char* value()
  {
    return "#robot status\n"
"uint8 id\n"
"uint8 level\n"
"uint16 remain_hp\n"
"uint16 max_hp\n"
"uint16 heat_cooling_limit\n"
"uint16 heat_cooling_rate\n"
"bool gimbal_output\n"
"bool chassis_output\n"
"bool shooter_output\n"
;
  }

  static const char* value(const ::roborts_msgs::RobotStatus_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::roborts_msgs::RobotStatus_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.id);
      stream.next(m.level);
      stream.next(m.remain_hp);
      stream.next(m.max_hp);
      stream.next(m.heat_cooling_limit);
      stream.next(m.heat_cooling_rate);
      stream.next(m.gimbal_output);
      stream.next(m.chassis_output);
      stream.next(m.shooter_output);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct RobotStatus_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::roborts_msgs::RobotStatus_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::roborts_msgs::RobotStatus_<ContainerAllocator>& v)
  {
    s << indent << "id: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.id);
    s << indent << "level: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.level);
    s << indent << "remain_hp: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.remain_hp);
    s << indent << "max_hp: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.max_hp);
    s << indent << "heat_cooling_limit: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.heat_cooling_limit);
    s << indent << "heat_cooling_rate: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.heat_cooling_rate);
    s << indent << "gimbal_output: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.gimbal_output);
    s << indent << "chassis_output: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.chassis_output);
    s << indent << "shooter_output: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.shooter_output);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ROBORTS_MSGS_MESSAGE_ROBOTSTATUS_H
