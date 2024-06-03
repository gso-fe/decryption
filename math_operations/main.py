# main.py

# Importieren der Module aus dem Unterordner 'operations'
from operations import add
from operations import multiply

def main():
    x = 5
    y = 3
    
    # Verwenden der Funktionen aus den importierten Modulen
    sum_result = add.add(x, y)
    product_result = multiply.multiply(x, y)
    
    print(f"Die Summe von {x} und {y} ist: {sum_result}")
    print(f"Das Produkt von {x} und {y} ist: {product_result}")

# Stellt sicher, dass main() nur ausgeführt wird, wenn main.py direkt gestartet wird
if __name__ == "__main__":
    main()

