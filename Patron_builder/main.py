from concrete_builder import ConcreteBuilder1
from director import Director
if __name__ == "__main__":

    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder

    print("Producto básico estándar: ")
    director.build_minimal_viable_product()
    builder.product.list_parts()

    print("\n")

    print("Producto estándar con todas las funciones: ")
    director.build_full_featured_product()
    builder.product.list_parts()

    print("\n")
    
    print("Producto Custom: ")
    builder.produce_part_a()
    builder.produce_part_b()
    builder.product.list_parts()