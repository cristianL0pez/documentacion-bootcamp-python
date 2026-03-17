TÍTULO DEL TEMA
Autor: Karen Ñanco Vásquez
Fecha: 17-03-2026
Issue relacionada: #40

📘 Definición
Poner nombres a las variables es el acto de asignar etiquetas descriptivas a los espacios de memoria donde guardamos datos. En programación, un "buen nombre" es aquel que explica qué contiene la variable sin necesidad de leer el resto del código.
Es la diferencia entre llamar a una caja "Cosa 1" o llamarla "Lista de invitados".

🧠 ¿Para qué sirve?
El código se lee muchas más veces de las que se escribe. Usar nombres claros es fundamental por tres razones:

1. Mantenibilidad: Permite que tú (u otros desarrolladores) entiendan el código meses después de haberlo escrito.
2. Reducción de errores: Si una variable se llama esUsuarioAdulto, es difícil que intentes guardarle un color por error.
3. Código autodocumentado: Minimiza la necesidad de escribir comentarios explicativos, ya que el código habla por sí mismo.

🧩 Sintaxis
En el desarrollo moderno, se prefiere la claridad sobre la brevedad. Evitamos letras únicas (como x o c) a menos que sean contadores de bucles muy específicos.

# ejemplo básico de sintaxis
// ❌ Malas prácticas
let d = 15; // ¿Días? ¿Distancia? ¿Dólares?
let lista = ["Juan", "Ana"]; // Muy genérico
let nmb_usr = "Alberth"; // Abreviatura confusa

// ✅ Buenas prácticas (Descriptivas y consistentes)
let diasParaVencimiento = 15;
let nombresDeEstudiantes = ["Juan", "Ana"];
let nombreDeUsuario = "Alberth";

*Reglas de oro*
1. Usa sustantivos para variables (precioTotal) y verbos para funciones (calcularPrecio).

2. Usa una convención estándar: Como camelCase (laSegundaPalabraEnMayuscula) o snake_case (palabras_con_guion_bajo).

3. Evita tecnicismos innecesarios: Prefiere esNombreValido sobre checkStringInputFormat.