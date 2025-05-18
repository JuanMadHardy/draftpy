import datetime

# 🎨 Decorador que envuelve cualquier función
def logger_decorator(func):
    def wrapper(*args, **kwargs):  # 🔄 Aquí está el wrapper
        print(f"Ejecutando '{func.__name__}' a las {datetime.datetime.now()}")
        resultado = func(*args, **kwargs)  # Ejecuta la función original
        print(f"Finalizando '{func.__name__}'")
        return resultado  # Devuelve el resultado de la función original
    return wrapper  # Devuelve el wrapper

# ✨ Aplicamos el decorador a una función
@logger_decorator
def saludar(nombre):
    print(f"Hola, {nombre}!")

# 🚀 Llamamos a la función decorada
saludar("Juan")