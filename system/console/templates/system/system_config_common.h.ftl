#define SYS_CONSOLE_DEVICE_MAX_INSTANCES   			${__INSTANCE_COUNT}
#define SYS_CONSOLE_UART_MAX_INSTANCES 	   			${SYS_CONSOLE_UART_CONNECTION_COUNTER}
#define SYS_CONSOLE_USB_CDC_MAX_INSTANCES 	   		${SYS_CONSOLE_USB_CONNECTION_COUNTER}

<#if SYS_CONSOLE_USB_CONNECTION_COUNTER != 0>
#define SYS_CONSOLE_USB_CDC_READ_WRITE_BUFFER_SIZE 	${SYS_CONSOLE_USB_READ_WRITE_BUFFER_SIZE}
</#if>