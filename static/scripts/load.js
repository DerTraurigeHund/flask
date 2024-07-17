// Funktion zum Anwenden des gespeicherten Themes
function applySavedTheme() {
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        document.documentElement.classList.add(savedTheme);
    } else {
        // Standardtheme, falls kein Theme im Local Storage gespeichert ist
        document.documentElement.classList.add('dark-theme');
    }
}

const themes = ['light-theme', 'dark-theme', 'blue-theme', 'green-theme', 'orange-theme', 'red-theme', 'yellow-theme', 'rainbow-theme', 'hacker-theme'];

// Funktion zum Wechseln des Themes und Speichern im Local Storage
function toggleTheme(theme) {
    if (!themes.includes(theme)) {
        theme = localStorage.getItem('theme') === 'dark-theme' ? 'light-theme' : 'dark-theme';
    }
    
    document.documentElement.classList.remove(...themes);
    document.documentElement.classList.add(theme);
    localStorage.setItem('theme', theme);
}


// Theme beim Laden der Seite anwenden
applySavedTheme();

function loadHeader() {
    const header = document.getElementById("head");
    if (!header) {
        console.error("Header element not found");
        return;
    }

    let logo = document.createElement("div");
    logo.classList.add("logo");

    let img = document.createElement("img");
    img.src = "/img/logo.png";
    img.alt = "Logo";
    img.style.width = "50px";
    img.style.height = "50px";
    logo.appendChild(img);

    let h1 = document.createElement("h1");
    h1.innerHTML = "GoldStudios.de";
    logo.appendChild(h1);
    header.appendChild(logo);

    let profile = document.createElement("div");
    profile.classList.add("profile");
    header.appendChild(profile);

    let dropdown = document.createElement("div");
    dropdown.classList.add("droppdown");
    profile.appendChild(dropdown);

    let img2 = document.createElement("img");
    img2.src = "/media/profiles/" + localStorage.getItem("username") + ".png"; // Passe diesen Pfad an
    img2.alt = "Profile Image"; // Hinzufügen eines Alt-Attributs
    dropdown.appendChild(img2);

    let dropdownContent = document.createElement("div");
    dropdownContent.classList.add("dropdown-content");
    dropdown.appendChild(dropdownContent);


    if (localStorage.getItem("username")) {
        let logout = document.createElement("a");
        logout.onclick = logout_;
        logout.style.cursor = "pointer";
        logout.innerHTML = "<i class='fas fa-sign-out-alt' style='vertical-align: middle;'></i> Logout";
        dropdownContent.appendChild(logout);
    } else {
        let login = document.createElement("a");
        login.href = "/login";
        login.innerHTML = "<i class='fas fa-sign-in-alt' style='vertical-align: middle;'></i> Login";
        dropdownContent.appendChild(login);
    }
}

function logout_() {
    localStorage.removeItem("username");
    localStorage.removeItem("id");
    window.location.href = "/logout";
}


document.addEventListener("DOMContentLoaded", loadHeader);