# JAVA PRIMITIVE DATA TYPES
# RANGE, FORMULA & CALCULATION


//================================================
//                  DATA TYPE
//================================================

// There are two basic types of data in Java

// 01 Primitive Data Type
// 02 Non-Primitive Data Type


//================================================
//                PRIMITIVE DATA TYPE
//================================================

// Java has 8 primitive data types

// 01 byte
// 02 short
// 03 char
// 04 int
// 05 long
// 06 float
// 07 double
// 08 boolean
//================================================
//                    RANGE
//================================================

// Range means the minimum and maximum value
// that a data type can store.

// Example:

// byte
// Minimum = -128
// Maximum = 127

// Therefore:
// byte range = -128 to 127


//================================================
//                     BITS
//================================================

// A bit is the smallest unit of data.

// A bit can have only two values:

// 0
// 1

// Therefore:

// 1 bit  = 2^1 = 2 possibilities
// 2 bits = 2^2 = 4 possibilities
// 3 bits = 2^3 = 8 possibilities
// 8 bits = 2^8 = 256 possibilities


//================================================
//          FORMULA FOR SIGNED INTEGER
//================================================

// Java uses signed integer types for:

// byte
// short
// int
// long

// Formula:

// Minimum = -2^(n - 1)
// Maximum =  2^(n - 1) - 1

// Here:
// n = number of bits


//================================================
//                    BYTE
//================================================

// byte uses 8 bits.

// Minimum:

// -2^(8 - 1)
// -2^7
// -128

// Maximum:

// 2^(8 - 1) - 1
// 2^7 - 1
// 128 - 1
// 127

// Therefore:

// byte = -128 to 127


//================================================
//                    SHORT
//================================================

// short uses 16 bits.

// Minimum:

// -2^(16 - 1)
// -2^15
// -32,768

// Maximum:

// 2^(16 - 1) - 1
// 2^15 - 1
// 32,768 - 1
// 32,767

// Therefore:

// short = -32,768 to 32,767


//================================================
//                     INT
//================================================

// int uses 32 bits.

// Minimum:

// -2^(32 - 1)
// -2^31
// -2,147,483,648

// Maximum:

// 2^(32 - 1) - 1
// 2^31 - 1
// 2,147,483,647

// Therefore:

// int = -2,147,483,648 to 2,147,483,647


//================================================
//                    LONG
//================================================

// long uses 64 bits.

// Minimum:

// -2^(64 - 1)
// -2^63
// -9,223,372,036,854,775,808

// Maximum:

// 2^(64 - 1) - 1
// 2^63 - 1
// 9,223,372,036,854,775,807

// Therefore:

// long = -9,223,372,036,854,775,808
//        to
//        9,223,372,036,854,775,807


//================================================
//                 WHY -1 IN MAXIMUM?
//================================================

// Suppose we have 3 bits.

// Total combinations:

// 2^3 = 8

// Values start from 0.

// Therefore:

// 0
// 1
// 2
// 3
// 4
// 5
// 6
// 7

// The maximum value is 7.

// Formula:

// 2^3 - 1
// 8 - 1
// 7

// Therefore, -1 is used because counting starts
// from zero.


//================================================
//              SIGNED RANGE EXPLANATION
//================================================

// Signed means the data type can store:

// Positive values
// Negative values
// Zero

// For example:

// byte = -128 to 127

// There are 256 total possible combinations.

// 2^8 = 256

// These combinations are distributed as:

// -128 to 127


//================================================
//                    CHAR
//================================================

// char uses 16 bits.

// char is an unsigned data type.

// Formula:

// Minimum = 0
// Maximum = 2^16 - 1

// Maximum:

// 2^16 - 1
// 65,536 - 1
// 65,535

// Therefore:

// char = 0 to 65,535


//================================================
//              FLOATING POINT TYPES
//================================================

// float and double are floating-point types.

// They do NOT use the same simple formula
// used by byte, short, int and long.

// They use a special floating-point
// representation.


# FLOAT

// float uses 32 bits.

// Approximate maximum finite value:

// 3.4028235 × 10^38

// Therefore:

// float ≈ ±3.4 × 10^38


# DOUBLE

// double uses 64 bits.

// Approximate maximum finite value:

// 1.7976931348623157 × 10^308

// Therefore:

// double ≈ ±1.7 × 10^308


//================================================
//                   BOOLEAN
//================================================

// boolean is different from numeric data types.

// boolean has only two possible values:

// true
// false


//================================================
//                TRUE AND FALSE
//================================================

// true means a condition is correct.

// false means a condition is not correct.

// Example:

// 10 > 5  = true
// 5 > 10  = false


//================================================
//           WHY BOOLEAN HAS NO RANGE?
//================================================

// boolean is NOT a numeric data type.

// byte, short, int and long have numeric ranges.

// Example:

// int = -2,147,483,648 to 2,147,483,647

// But boolean only has two logical values:

// true
// false

// Therefore, Java does not define a numeric range
// for boolean.

// IMPORTANT:

// true  != 1
// false != 0

// In Java, true and false are boolean values,
// not integer values.


//================================================
//             FIND RANGE THROUGH CODE
//================================================

// Java provides predefined constants to find
// minimum and maximum values.

// byte:

// Byte.MIN_VALUE
// Byte.MAX_VALUE

// short:

// Short.MIN_VALUE
// Short.MAX_VALUE

// int:

// Integer.MIN_VALUE
// Integer.MAX_VALUE

// long:

// Long.MIN_VALUE
// Long.MAX_VALUE

// float:

// Float.MIN_VALUE
// Float.MAX_VALUE

// double:

// Double.MIN_VALUE
// Double.MAX_VALUE

// char:

// Character.MIN_VALUE
// Character.MAX_VALUE


//================================================
//               IMPORTANT FLOAT NOTE
//================================================

// Float.MIN_VALUE does NOT mean the most negative
// float value.

// Float.MIN_VALUE means the smallest positive
// non-zero float value.

// Similarly:

// Double.MIN_VALUE means the smallest positive
// non-zero double value.

// For the most negative approximate values:

// -Float.MAX_VALUE
// -Double.MAX_VALUE


//================================================
//              RANGE SUMMARY
//================================================

// byte:
// 8 bits
// -128 to 127

// short:
// 16 bits
// -32,768 to 32,767

// char:
// 16 bits
// 0 to 65,535

// int:
// 32 bits
// -2,147,483,648 to 2,147,483,647

// long:
// 64 bits
// -9,223,372,036,854,775,808
// to
// 9,223,372,036,854,775,807

// float:
// 32 bits
// Approximately ±3.4 × 10^38

// double:
// 64 bits
// Approximately ±1.7 × 10^308

// boolean:
// true or false


//================================================
//                MOST IMPORTANT FORMULA
//================================================

// For signed integer types:

// Minimum = -2^(n - 1)
// Maximum =  2^(n - 1) - 1

// Where:

// n = number of bits


//================================================
//                 QUICK MEMORY
//================================================

// byte    = 8 bits
// short   = 16 bits
// char    = 16 bits
// int     = 32 bits
// long    = 64 bits
// float   = 32 bits
// double  = 64 bits
// boolean = true / false


//================================================
//                    SUMMARY
//================================================

// Whole Numbers:

// byte
// short
// int
// long

// Decimal Numbers:

// float
// double

// Single Character:

// char

// Logical Values:

// boolean


//================================================
//                    END
//================================================