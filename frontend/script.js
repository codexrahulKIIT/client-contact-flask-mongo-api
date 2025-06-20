const API_URL = "http://127.0.0.1:5000/clients";

document.getElementById("clientForm").addEventListener("submit", function (e) {
  e.preventDefault();
  const client = {
    name: document.getElementById("name").value,
    email: document.getElementById("email").value,
    company: document.getElementById("company").value,
    phone: document.getElementById("phone").value,
    status: document.getElementById("status").value,
  };

  fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(client)
  }).then(() => {
    loadClients();
    this.reset();
  });
});

function loadClients() {
  fetch(API_URL)
    .then(res => res.json())
    .then(data => {
      const tbody = document.getElementById("clientList");
      tbody.innerHTML = "";
      data.forEach(client => {
        tbody.innerHTML += `
          <tr>
            <td>${client.name}</td>
            <td>${client.email}</td>
            <td>${client.company}</td>
            <td>${client.phone}</td>
            <td>${client.status}</td>
            <td>
              <button class="delete-btn" onclick="deleteClient('${client._id.$oid || client._id}')">Delete</button>
            </td>
          </tr>
        `;
      });
    });
}

function deleteClient(id) {
  fetch(`${API_URL}/${id}`, {
    method: "DELETE"
  }).then(() => loadClients());
}

// Initial load
loadClients();
