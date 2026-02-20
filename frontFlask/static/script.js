
const API_URL = "http://127.0.0.1:5000/v1/usuarios/";

async function cargarUsuarios() {
    const res = await fetch(API_URL);
    const data = await res.json();
    const tbody = document.querySelector("#usuariosTable tbody");
    tbody.innerHTML = "";

    data.Usuarios.forEach(usuario => {
        const tr = document.createElement("tr");
        tr.innerHTML = `
            <td>${usuario.id}</td>
            <td>${usuario.nombre}</td>
            <td>${usuario.edad}</td>
            <td>
                <button class="edit" onclick="editarUsuario(${usuario.id})">Editar</button>
                <button class="delete" onclick="eliminarUsuario(${usuario.id})">Eliminar</button>
            </td>
        `;
        tbody.appendChild(tr);
    });
}

document.getElementById("addUserForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    const usuario = {
        id: parseInt(document.getElementById("id").value),
        nombre: document.getElementById("nombre").value,
        edad: parseInt(document.getElementById("edad").value)
    };

    await fetch(API_URL, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(usuario)
    });

    cargarUsuarios();
    e.target.reset();
});

async function eliminarUsuario(id) {
    const confirmar = confirm("¿Seguro que deseas eliminar este usuario?");
    if (confirmar) {
        await fetch(`${API_URL}${id}`, { method: "DELETE" });
        cargarUsuarios();
    }
}

async function editarUsuario(id) {
    const nuevoNombre = prompt("Nuevo nombre:");
    const nuevaEdad = prompt("Nueva edad:");

    if (nuevoNombre && nuevaEdad) {
        await fetch(`${API_URL}${id}`, {
            method: "PUT",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({ nombre: nuevoNombre, edad: parseInt(nuevaEdad) })
        });
        cargarUsuarios();
    }
}

// Inicializar
cargarUsuarios();