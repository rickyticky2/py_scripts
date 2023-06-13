import os
import yaml

# Читаем конфигурацию сервисов из YAML файла
with open("services.yaml", "r") as f:
    services = yaml.safe_load(f)

# Корневая директория, где находятся папки с кодом и jar файлами
root_dir = "/root/Projects/test"

for service_name, service_config in services.items():
    # Создаем Dockerfile
    dockerfile_content = f"""
        FROM openjdk:8-jdk-alpine
        
        WORKDIR /app
        
        COPY {service_name}/*.java ./app.jar    
        
        EXPOSE {' '.join(service_config['ports'])}
        
        CMD ["exec", "java", "{service_config['java_opts']}", "{service_name}"]
    """
    
    # Создаем Dockerfile в папке сервиса
    with open(os.path.join(root_dir, service_name, "Dockerfile"), "w") as f:
        f.write(dockerfile_content)
