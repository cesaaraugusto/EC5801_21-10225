/**
 * Generated Pins header File
 * 
 * @file pins.h
 * 
 * @defgroup  pinsdriver Pins Driver
 * 
 * @brief This is generated driver header for pins. 
 *        This header file provides APIs for all pins selected in the GUI.
 *
 * @version Driver Version  3.0.0
*/

/*
© [2026] Microchip Technology Inc. and its subsidiaries.

    Subject to your compliance with these terms, you may use Microchip 
    software and any derivatives exclusively with Microchip products. 
    You are responsible for complying with 3rd party license terms  
    applicable to your use of 3rd party software (including open source  
    software) that may accompany Microchip software. SOFTWARE IS ?AS IS.? 
    NO WARRANTIES, WHETHER EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS 
    SOFTWARE, INCLUDING ANY IMPLIED WARRANTIES OF NON-INFRINGEMENT,  
    MERCHANTABILITY, OR FITNESS FOR A PARTICULAR PURPOSE. IN NO EVENT 
    WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE, 
    INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY 
    KIND WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF 
    MICROCHIP HAS BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE 
    FORESEEABLE. TO THE FULLEST EXTENT ALLOWED BY LAW, MICROCHIP?S 
    TOTAL LIABILITY ON ALL CLAIMS RELATED TO THE SOFTWARE WILL NOT 
    EXCEED AMOUNT OF FEES, IF ANY, YOU PAID DIRECTLY TO MICROCHIP FOR 
    THIS SOFTWARE.
*/

#ifndef PINS_H
#define PINS_H

#include <xc.h>

#define INPUT   1
#define OUTPUT  0

#define HIGH    1
#define LOW     0

#define ANALOG      1
#define DIGITAL     0

#define PULL_UP_ENABLED      1
#define PULL_UP_DISABLED     0

// get/set IO_RC0 aliases
#define IO_RC0_TRIS                 TRISCbits.TRISC0
#define IO_RC0_LAT                  LATCbits.LATC0
#define IO_RC0_PORT                 PORTCbits.RC0
#define IO_RC0_WPU                  WPUCbits.WPUC0
#define IO_RC0_OD                   ODCONCbits.ODCC0
#define IO_RC0_ANS                  ANSELCbits.ANSC0
#define IO_RC0_SetHigh()            do { LATCbits.LATC0 = 1; } while(0)
#define IO_RC0_SetLow()             do { LATCbits.LATC0 = 0; } while(0)
#define IO_RC0_Toggle()             do { LATCbits.LATC0 = ~LATCbits.LATC0; } while(0)
#define IO_RC0_GetValue()           PORTCbits.RC0
#define IO_RC0_SetDigitalInput()    do { TRISCbits.TRISC0 = 1; } while(0)
#define IO_RC0_SetDigitalOutput()   do { TRISCbits.TRISC0 = 0; } while(0)
#define IO_RC0_SetPullup()          do { WPUCbits.WPUC0 = 1; } while(0)
#define IO_RC0_ResetPullup()        do { WPUCbits.WPUC0 = 0; } while(0)
#define IO_RC0_SetPushPull()        do { ODCONCbits.ODCC0 = 0; } while(0)
#define IO_RC0_SetOpenDrain()       do { ODCONCbits.ODCC0 = 1; } while(0)
#define IO_RC0_SetAnalogMode()      do { ANSELCbits.ANSC0 = 1; } while(0)
#define IO_RC0_SetDigitalMode()     do { ANSELCbits.ANSC0 = 0; } while(0)
// get/set IO_RC2 aliases
#define LED_TRIS                 TRISCbits.TRISC2
#define LED_LAT                  LATCbits.LATC2
#define LED_PORT                 PORTCbits.RC2
#define LED_WPU                  WPUCbits.WPUC2
#define LED_OD                   ODCONCbits.ODCC2
#define LED_ANS                  ANSELCbits.ANSC2
#define LED_SetHigh()            do { LATCbits.LATC2 = 1; } while(0)
#define LED_SetLow()             do { LATCbits.LATC2 = 0; } while(0)
#define LED_Toggle()             do { LATCbits.LATC2 = ~LATCbits.LATC2; } while(0)
#define LED_GetValue()           PORTCbits.RC2
#define LED_SetDigitalInput()    do { TRISCbits.TRISC2 = 1; } while(0)
#define LED_SetDigitalOutput()   do { TRISCbits.TRISC2 = 0; } while(0)
#define LED_SetPullup()          do { WPUCbits.WPUC2 = 1; } while(0)
#define LED_ResetPullup()        do { WPUCbits.WPUC2 = 0; } while(0)
#define LED_SetPushPull()        do { ODCONCbits.ODCC2 = 0; } while(0)
#define LED_SetOpenDrain()       do { ODCONCbits.ODCC2 = 1; } while(0)
#define LED_SetAnalogMode()      do { ANSELCbits.ANSC2 = 1; } while(0)
#define LED_SetDigitalMode()     do { ANSELCbits.ANSC2 = 0; } while(0)
// get/set IO_RC3 aliases
#define SWITCH_TRIS                 TRISCbits.TRISC3
#define SWITCH_LAT                  LATCbits.LATC3
#define SWITCH_PORT                 PORTCbits.RC3
#define SWITCH_WPU                  WPUCbits.WPUC3
#define SWITCH_OD                   ODCONCbits.ODCC3
#define SWITCH_ANS                  ANSELCbits.ANSC3
#define SWITCH_SetHigh()            do { LATCbits.LATC3 = 1; } while(0)
#define SWITCH_SetLow()             do { LATCbits.LATC3 = 0; } while(0)
#define SWITCH_Toggle()             do { LATCbits.LATC3 = ~LATCbits.LATC3; } while(0)
#define SWITCH_GetValue()           PORTCbits.RC3
#define SWITCH_SetDigitalInput()    do { TRISCbits.TRISC3 = 1; } while(0)
#define SWITCH_SetDigitalOutput()   do { TRISCbits.TRISC3 = 0; } while(0)
#define SWITCH_SetPullup()          do { WPUCbits.WPUC3 = 1; } while(0)
#define SWITCH_ResetPullup()        do { WPUCbits.WPUC3 = 0; } while(0)
#define SWITCH_SetPushPull()        do { ODCONCbits.ODCC3 = 0; } while(0)
#define SWITCH_SetOpenDrain()       do { ODCONCbits.ODCC3 = 1; } while(0)
#define SWITCH_SetAnalogMode()      do { ANSELCbits.ANSC3 = 1; } while(0)
#define SWITCH_SetDigitalMode()     do { ANSELCbits.ANSC3 = 0; } while(0)
#define RC3_SetInterruptHandler  SWITCH_SetInterruptHandler
/**
 * @ingroup  pinsdriver
 * @brief GPIO and peripheral I/O initialization
 * @param none
 * @return none
 */
void PIN_MANAGER_Initialize (void);

/**
 * @ingroup  pinsdriver
 * @brief Interrupt on Change Handling routine
 * @param none
 * @return none
 */
void PIN_MANAGER_IOC(void);

/**
 * @ingroup  pinsdriver
 * @brief Interrupt on Change Handler for the SWITCH pin functionality
 * @param none
 * @return none
 */
void SWITCH_ISR(void);

/**
 * @ingroup  pinsdriver
 * @brief Interrupt Handler Setter for SWITCH pin interrupt-on-change functionality.
 *        Allows selecting an interrupt handler for SWITCH at application runtime.
 * @pre Pins intializer called
 * @param InterruptHandler function pointer.
 * @return none
 */
void SWITCH_SetInterruptHandler(void (* InterruptHandler)(void));

/**
 * @ingroup  pinsdriver
 * @brief Dynamic Interrupt Handler for SWITCH pin.
 *        This is a dynamic interrupt handler to be used together with the SWITCH_SetInterruptHandler() method.
 *        This handler is called every time the SWITCH ISR is executed and allows any function to be registered at runtime.
 * @pre Pins intializer called
 * @param none
 * @return none
 */
extern void (*SWITCH_InterruptHandler)(void);

/**
 * @ingroup  pinsdriver
 * @brief Default Interrupt Handler for SWITCH pin. 
 *        This is a predefined interrupt handler to be used together with the SWITCH_SetInterruptHandler() method.
 *        This handler is called every time the SWITCH ISR is executed. 
 * @pre Pins intializer called
 * @param none
 * @return none
 */
void SWITCH_DefaultInterruptHandler(void);


#endif // PINS_H
/**
 End of File
*/