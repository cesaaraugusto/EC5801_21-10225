 /*
 * MAIN Generated Driver File
 * 
 * @file main.c
 * 
 * @defgroup main MAIN
 * 
 * @brief This is the generated driver implementation file for the MAIN driver.
 *
 * @version MAIN Driver Version 1.0.2
 *
 * @version Package Version: 3.1.2
*/

/*
� [2026] Microchip Technology Inc. and its subsidiaries.

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
#include "mcc_generated_files/system/pins.h"
#include "mcc_generated_files/system/system.h"
#include "mcc_generated_files/timer/tmr0.h"
#include <stdint.h>
    
#define CONSTANT_1 0xff
#define DUTY_CYCLE_BASIC 128
    
int contador = 0;

/* Callbacks */
void TMR0_Callback(void){
    LED_Toggle();
}


void switch_interrupt(void){
    contador++;
    if (contador >= 8){
        contador = 0;
        PWM1_LoadDutyValue(DUTY_CYCLE_BASIC);
    } else {
        uint16_t new_duty_cycle = ((uint16_t)contador * DUTY_CYCLE_BASIC);
        PWM1_LoadDutyValue(new_duty_cycle);
    }
            
        }
        
        /*
        Main application
        */
        
        int main(void)
        {
            SYSTEM_Initialize();
            
            // Enable the Global Interrupts 
            INTERRUPT_GlobalInterruptEnable(); 
            
            
            // Enable the Peripheral Interrupts 
            INTERRUPT_PeripheralInterruptEnable(); 
            
            //Defining interruption
            SWITCH_SetInterruptHandler(switch_interrupt);
            
            TMR0_PeriodMatchCallbackRegister(TMR0_Callback);
            TMR0_TMRInterruptEnable();
            TMR0_Start();
            TMR2_Start();
            
    while(1){
       // SLEEP();
    }    
}

