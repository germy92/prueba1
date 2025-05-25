@echo off
cd /d D:\lab_django
echo "Escribe el mensaje del commit:"
read mensaje
git add .
git commit -m "$mensaje %date% %time%"
git push origin main