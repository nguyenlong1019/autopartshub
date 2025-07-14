function showToast(msg, type, timems) {
    const container = document.getElementById('toast-container');
    const toast = document.createElement('div');
    toast.className = `toast ${type}`;
    toast.innerText = msg;
    container.appendChild(toast);

    setTimeout(() => {
      toast.remove();
    }, timems);
}

function gcsrf() {
  return document.querySelector('[name=csrfmiddlewaretoken]').value;
}

function isValidEmail(email) {
  const regex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
  return regex.test(email);
}