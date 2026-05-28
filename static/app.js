async function addTask() {
  const input = document.getElementById("task-input");
  const title = input.value.trim();

  if (!title) {
    alert("Please enter a task.");
    return;
  }

  const response = await fetch("/api/tasks", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ title })
  });

  const data = await response.json();

  if (!response.ok) {
    document.getElementById("output").textContent = JSON.stringify(data, null, 2);
    return;
  }

  const li = document.createElement("li");
  li.textContent = data.title;
  document.getElementById("task-list").appendChild(li);
  input.value = "";
}

async function checkHealth() {
  const response = await fetch("/api/health");
  const data = await response.json();
  document.getElementById("output").textContent = JSON.stringify(data, null, 2);
}
