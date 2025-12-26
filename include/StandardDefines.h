#ifndef STANDARDEFINES_H
#define STANDARDEFINES_H

#include <string>
#include <optional>
#include <vector>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <queue>
#include <stack>
#include <deque>
#include <list>
#include <array>

using std::vector;
using std::unordered_map;
using std::set;
using std::unordered_set;
using std::queue;
using std::stack;
using std::deque;
using std::list;
using std::array;

// Arduino/ESP32 compatible map type as Arduino.h already has a map type
template <typename K, typename V> 
using std_map = std::map<K, V>;

// Arduino/ESP32 compatible integer types
typedef int Int;
typedef const int CInt;
typedef unsigned int UInt;
typedef const unsigned int CUInt;
typedef long Long;
typedef const long CLong;
typedef unsigned long ULong;
typedef const unsigned long CULong;
typedef unsigned char UInt8;

// Character types
typedef char Char;
typedef const char CChar;
typedef unsigned char UChar;
typedef const unsigned char CUChar;

// Boolean type
typedef bool Bool;
typedef const bool CBool;

// Size type
typedef size_t Size;
typedef const size_t CSize;

// Pointer types
typedef void* VoidPtr;
typedef const void* CVoidPtr;
typedef void Void;

// String types
typedef std::string StdString;
typedef const std::string CStdString;
using std::optional;

#define Var auto
#define Val const auto
#define Const constexpr auto

#define Private public: private:
#define Protected public: protected:
#define Public private: public:
#define Static static
#define Virtual virtual
#define Explicit explicit
#define NoDiscard [[nodiscard]]

// Standard pointers
#include <memory>
using std::shared_ptr;
using std::unique_ptr;
using std::weak_ptr;

using std::make_shared;

#define DefineStandardPointers(class_name) \
    class class_name; \
    typedef const class_name C##class_name; \
    typedef shared_ptr<class_name> class_name##SPtr; \
    typedef const shared_ptr<class_name> C##class_name##SPtr; \
    typedef weak_ptr<class_name> class_name##WPtr; \
    typedef const weak_ptr<class_name> C##class_name##WPtr; \
    typedef shared_ptr<class_name> class_name##Ptr; \
    typedef const shared_ptr<class_name> C##class_name##Ptr;

#define make_ptr std::make_shared

#define DefineStandardTypes(enum_name) \
    enum class enum_name; \
    typedef const enum_name C##enum_name;

// These macros are used by the preprocessing scripts
// They need to be defined for compilation to work
#define COMPONENT
#define AUTOWIRED  
#define INTERFACE
#define SCOPE(SCOPE_TYPE)
#define VALIDATE_WITH(CLASS_NAME)
#define VALIDATE

// Template declaration for Implementation
template <class T>
struct Implementation;

#endif // STANDARDEFINES_H