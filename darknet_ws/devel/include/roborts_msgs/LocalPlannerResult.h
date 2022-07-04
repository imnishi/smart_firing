// Generated by gencpp from file roborts_msgs/LocalPlannerResult.msg
// DO NOT EDIT!


#ifndef ROBORTS_MSGS_MESSAGE_LOCALPLANNERRESULT_H
#define ROBORTS_MSGS_MESSAGE_LOCALPLANNERRESULT_H


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
struct LocalPlannerResult_
{
  typedef LocalPlannerResult_<ContainerAllocator> Type;

  LocalPlannerResult_()
    : error_code(0)  {
    }
  LocalPlannerResult_(const ContainerAllocator& _alloc)
    : error_code(0)  {
  (void)_alloc;
    }



   typedef int32_t _error_code_type;
  _error_code_type error_code;





  typedef boost::shared_ptr< ::roborts_msgs::LocalPlannerResult_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::roborts_msgs::LocalPlannerResult_<ContainerAllocator> const> ConstPtr;

}; // struct LocalPlannerResult_

typedef ::roborts_msgs::LocalPlannerResult_<std::allocator<void> > LocalPlannerResult;

typedef boost::shared_ptr< ::roborts_msgs::LocalPlannerResult > LocalPlannerResultPtr;
typedef boost::shared_ptr< ::roborts_msgs::LocalPlannerResult const> LocalPlannerResultConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::roborts_msgs::LocalPlannerResult_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::roborts_msgs::LocalPlannerResult_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::roborts_msgs::LocalPlannerResult_<ContainerAllocator1> & lhs, const ::roborts_msgs::LocalPlannerResult_<ContainerAllocator2> & rhs)
{
  return lhs.error_code == rhs.error_code;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::roborts_msgs::LocalPlannerResult_<ContainerAllocator1> & lhs, const ::roborts_msgs::LocalPlannerResult_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace roborts_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::roborts_msgs::LocalPlannerResult_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::roborts_msgs::LocalPlannerResult_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::roborts_msgs::LocalPlannerResult_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::roborts_msgs::LocalPlannerResult_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::roborts_msgs::LocalPlannerResult_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::roborts_msgs::LocalPlannerResult_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::roborts_msgs::LocalPlannerResult_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ea324a22c787839f822b9a025bc2c6fe";
  }

  static const char* value(const ::roborts_msgs::LocalPlannerResult_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xea324a22c787839fULL;
  static const uint64_t static_value2 = 0x822b9a025bc2c6feULL;
};

template<class ContainerAllocator>
struct DataType< ::roborts_msgs::LocalPlannerResult_<ContainerAllocator> >
{
  static const char* value()
  {
    return "roborts_msgs/LocalPlannerResult";
  }

  static const char* value(const ::roborts_msgs::LocalPlannerResult_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::roborts_msgs::LocalPlannerResult_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"#result definition RUNNING = 0, SUCCESS = 1, FAILURE = 2\n"
"int32  error_code\n"
;
  }

  static const char* value(const ::roborts_msgs::LocalPlannerResult_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::roborts_msgs::LocalPlannerResult_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.error_code);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct LocalPlannerResult_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::roborts_msgs::LocalPlannerResult_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::roborts_msgs::LocalPlannerResult_<ContainerAllocator>& v)
  {
    s << indent << "error_code: ";
    Printer<int32_t>::stream(s, indent + "  ", v.error_code);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ROBORTS_MSGS_MESSAGE_LOCALPLANNERRESULT_H
