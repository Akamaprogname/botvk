<?php

define('BOT_BASE_DIRECTORY', '/var/www');
define('BOT_LOGS_DIRECTORY', BOT_BASE_DIRECTORY.'/logs');
define('BOT_IMAGES_DIRECTORY', BOT_BASE_DIRECTORY.'/static');
define('BOT_AUDIO_DIRECTORY', BOT_BASE_DIRECTORY.'/audio');

define('CALLBACK_API_CONFIRMATION_TOKEN', getenv('CALLBACK_API_CONFIRMATION_TOKEN')); //Строка для подтверждения адреса сервера из настроек Callback API
define('VK_API_ACCESS_TOKEN', getenv('VK_API_ACCESS_TOKEN')); //Ключ доступа сообщества
