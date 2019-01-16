# Namecheap DNS Updater

Lack of information...

## IP Information

Get my local server public ip address:
 - dig +short myip.opendns.com @resolver1.opendns.com

Get the ip address for my domain (for comparison)
 - dig +short < yourdomain.here >


## Request

https://dynamicdns.park-your-domain.com/update?host=@&domain=< yourdomain.here >&password=< yourkeypassword >&ip=< yourpublicip >

## Sucess Reply

	<?xml version="1.0" encoding="UTF-8"?>
	<interface-response>
	   <Command>SETDNSHOST</Command>
	   <Language>eng</Language>
	   <IP>xxw.yyy.www.zzz</IP>
	   <ErrCount>0</ErrCount>
	   <ResponseCount>0</ResponseCount>
	   <Done>true</Done>
	   <debug />
	</interface-response>

## Error (in password)

	<?xml version="1.0" encoding="UTF-8"?>
	<interface-response>
	   <Command>SETDNSHOST</Command>
	   <Language>eng</Language>
	   <ErrCount>1</ErrCount>
	   <errors>
	      <Err1>Passwords do not match</Err1>
	   </errors>
	   <ResponseCount>1</ResponseCount>
	   <responses>
	      <response>
		 <ResponseNumber>304156</ResponseNumber>
		 <ResponseString>Validation error; invalid ; password</ResponseString>
	      </response>
	   </responses>
	   <Done>true</Done>
	   <debug />
	</interface-response>


