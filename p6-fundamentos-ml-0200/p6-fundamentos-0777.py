# ==========================================
# 1. Python Variables
# ==========================================

# Ejemplo 1: Creación de variables simples
nombre = "Alejandra"
edad = 20
estatura = 1.65
print(f"Nombre: {nombre}, Edad: {edad}, Estatura: {estatura}")

# Ejemplo 2: Cambio de tipo de dato (tipado dinámico)
x = 10
print(f"x (int): {x}")
x = "Python"
print(f"x (str): {x}")

# Ejemplo 3: Casting
a, b, c = str(5), int(5), float(5)
print(f"a: '{a}', b: {b}, c: {c}")

print("A-A-A-A-A-A-A-A-A-A-A-A")

# ==========================================
# 2. Assign Multiple Values
# ==========================================

# Ejemplo 1: Múltiples valores a múltiples variables
fruta1, fruta2, fruta3 = "Manzana", "Plátano", "Cereza"
print(f"Frutas: {fruta1}, {fruta2}, {fruta3}")

# Ejemplo 2: Un mismo valor a múltiples variables
v1 = v2 = v3 = "Python"
print(f"Mismo valor: {v1}, {v2}, {v3}")

# Ejemplo 3: Desempaquetar una lista
colores = ["Rojo", "Verde", "Azul"]
c1, c2, c3 = colores
print(f"Colores: {c1}, {c2}, {c3}")

print("A-A-A-A-A-A-A-A-A-A-A-A")

# ==========================================
# 3. Data Types: Text & Numeric
# ==========================================

# Ejemplo 1: String (str)
texto = "Hola Mundo"
print(f"Texto: {texto} ({type(texto)})")

# Ejemplo 2: Integer (int)
numero = 42
print(f"Entero: {numero} ({type(numero)})")

# Ejemplo 3: Float (float)
decimal = 3.1416
print(f"Decimal: {decimal} ({type(decimal)})")

print("A-A-A-A-A-A-A-A-A-A-A-A")

# ==========================================
# 4. Data Types: Sequences
# ==========================================

# Ejemplo 1: List
lista = ["manzana", "pera", "uva"]
print(f"Lista: {lista}")

# Ejemplo 2: Tuple
tupla = (10, 20, 30)
print(f"Tupla: {tupla}")

# Ejemplo 3: Range
rango = range(1, 4)
print(f"Rango: {list(rango)}")

print("A-A-A-A-A-A-A-A-A-A-A-A")

# ==========================================
# 5. Data Types: Dict, Set & Bool
# ==========================================

# Ejemplo 1: Dictionary (dict)
estudiante = {"nombre": "Alejandra", "nc": "0200"}
print(f"Diccionario: {estudiante}")

# Ejemplo 2: Set (set)
conjunto = {1, 2, 3}
print(f"Conjunto: {conjunto}")

# Ejemplo 3: Boolean (bool)
es_activo = True
print(f"Booleano: {es_activo}")

print("A-A-A-A-A-A-A-A-A-A-A-A")

# ==========================================
# 6. Arithmetic Operators
# ==========================================

# Ejemplo 1: Suma y Resta
suma, resta = 15 + 5, 20 - 8
print(f"Suma: {suma}, Resta: {resta}")

# Ejemplo 2: Multiplicación y División
multi, div = 4 * 3, 10 / 3
print(f"Multiplicación: {multi}, División: {div}")

# Ejemplo 3: Módulo, Potencia y División Entera
mod, pot, div_ent = 10 % 3, 2 ** 3, 10 // 3
print(f"Módulo: {mod}, Potencia: {pot}, Div. Entera: {div_ent}")

print("A-A-A-A-A-A-A-A-A-A-A-A")

# ==========================================
# 7. Assignment Operators
# ==========================================

# Ejemplo 1: Asignación simple (=) y Suma (+=)
num = 10
num += 5
print(f"num tras += 5: {num}")

# Ejemplo 2: Resta (-=) y Multiplicación (*=)
num -= 3
num *= 2
print(f"num tras -= 3 y *= 2: {num}")

# Ejemplo 3: División (/=) y Exponente (**=)
num /= 4
num **= 2
print(f"num tras /= 4 y **= 2: {num}")

print("A-A-A-A-A-A-A-A-A-A-A-A")

# ==========================================
# 8. Comparison Operators
# ==========================================

# Ejemplo 1: Igualdad (==) y Desigualdad (!=)
print(f"10 == 10: {10 == 10}, 10 != 5: {10 != 5}")

# Ejemplo 2: Mayor que (>) y Menor que (<)
print(f"15 > 20: {15 > 20}, 5 < 10: {5 < 10}")

# Ejemplo 3: Mayor o igual (>=) y Menor o igual (<=)
print(f"10 >= 10: {10 >= 10}, 8 <= 5: {8 <= 5}")

print("A-A-A-A-A-A-A-A-A-A-A-A")

# ==========================================
# 9. Logical Operators
# ==========================================

# Ejemplo 1: AND
and_res = (5 > 3) and (10 > 5)
print(f"(5 > 3) and (10 > 5): {and_res}")

# Ejemplo 2: OR
or_res = (5 > 10) or (10 > 5)
print(f"(5 > 10) or (10 > 5): {or_res}")

# Ejemplo 3: NOT
not_res = not(5 > 3)
print(f"not(5 > 3): {not_res}")

print("A-A-A-A-A-A-A-A-A-A-A-A")