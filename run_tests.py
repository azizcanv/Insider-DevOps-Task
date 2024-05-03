import subprocess
import sys

def run_tests(node_count):
    """
    Belirtilen düğüm sayısına göre Docker konteynerlerini başlatır ve testleri çalıştırır.
    """
    # Docker konteynerlerini başlat
    subprocess.run(["docker-compose", "up", "-d", "--scale", f"selenium-node-chrome={node_count}"])
    
    # Testleri çalıştır
    subprocess.run(["python", "-m", "pytest", "--html=report.html"])

    # Docker konteynerlerini kapat
    subprocess.run(["docker-compose", "down"])

if __name__ == "__main__":
    # Düğüm sayısını belirle
    node_count = int(sys.argv[1]) if len(sys.argv) > 1 else 1

    # Testleri belirtilen düğüm sayısıyla çalıştır
    run_tests(node_count)
