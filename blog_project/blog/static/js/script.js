function logout() {
    localStorage.removeItem('access');
    localStorage.removeItem('refresh');
    localStorage.removeItem('username');
    window.location.href = '/login/';
}

function capitalize(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}