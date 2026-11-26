#!/bin/bash
echo "Проверяю папку $1"
if ls "$1"; then 
	ls "$1"
echo "Код: $?"
else
	echo "Ошибка"
fi
