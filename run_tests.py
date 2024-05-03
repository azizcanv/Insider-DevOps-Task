import subprocess
import time
import sys

def check_grid_health():
    """
    Selenium Grid sağlığını kontrol etmek için bir işlev.
    Selenium Grid sağlıklı bir şekilde çalışıyorsa True döndürür, aksi takdirde False döndürür.
    """
    try:
        subprocess.run(["docker", "ps"], check=True)
        # Selenium Grid konteynerleri çalışıyor, sağlıklı
        return True
    except subprocess.CalledProcessError:
        # Selenium Grid konteynerleri çalışmıyor, sağlıksız
        return False

def run_tests(node_count):
    """
    Belirtilen düğüm sayısına göre Docker konteynerlerini başlatır ve testleri çalıştırır.
    """
    # Selenium Grid sağlığını kontrol et
    if not check_grid_health():
        print("Selenium Grid is not healthy. Aborting test execution.")
        return
    
    # Docker konteynerlerini başlat
    subprocess.run(["docker-compose", "up", "-d", "--scale", f"selenium-node-chrome={node_count}"])
    
    subprocess.run(["docker", "ps", "-a"])
    
    # Selenium konteynerinde testleri çalıştır ve rapor oluştur
    subprocess.run(["docker-compose", "exec", "jenkinstask", "sh", "-c", "python -m pytest --html=/app/report.html"])

    # Docker konteynerlerini kapat
    subprocess.run(["docker-compose", "down"])

    # Oluşturulan raporu dışarı aktar
    subprocess.run(["docker", "cp", "jenkinstask:/app/report.html", "./report.html"])

if __name__ == "__main__":
    # Düğüm sayısını belirle
    node_count = int(sys.argv[1]) if len(sys.argv) > 1 else 1

    # Testleri belirtilen düğüm sayısıyla çalıştır
    run_tests(node_count)