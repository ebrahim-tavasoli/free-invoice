# Accounting application

## installation:
#### docker compose:
Set configuration in docker-compose.yml
then execute with following command.

```
docker-compose up -d
```

## Configuration:
- If you want use sms (Kavenegar supported only) you must set kavenegar API key and sender number.
- If you want use email feature you must set email settings.
- If you want use payment gateway (Bahamta supported only) you must set API key and call back url 
(by setting DOMAIN_WITH_SCHEME in environment variables of docker-compose.yml file the callback url
will generate like 'http(s)://\<domain\>/payment/callback/').
- The default database is sqlite if you want use another database can change database setting.
#### Supported database:
- sqlite
- postgresql
- mysql/mariadb
- oracel

The project configured with postgresql by default.

#### Default username and password:
```
username: admin
password: admin
```