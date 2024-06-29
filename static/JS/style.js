
function toggleclass(tagname) {
    const tagnam = document.querySelector(tagname);
    tagnam.classList.toggle('hidden');
}

function hrefgen(page) {
    window.location.href = window.location.origin + "/" + page;
}

function toggleMenu() {
    const navLinks = document.querySelector('nav');
    // navLinks.classList.toggle('hidden');
    const classess = "hidden flex-col py-24"
    const classlist = classess.split(" ")
    if (navLinks.classList.contains("hidden")) {
        classlist.forEach(element => {
            navLinks.classList.remove(element)
        });
        // navLinks.classList.remove("flex-col","text-red-900")
    } else {
        classlist.forEach(element => {
            navLinks.classList.add(element)
        });
        // navLinks.classList.add("flex-col")
    }
}

const currenthref = window.location.href;
if (currenthref != window.location.origin+"/") {
    document.querySelectorAll("header div nav a").forEach((e) => {
        e.href = window.location.origin + e.getAttribute("href").replace("#", "/")
    });
}
function loaderpage() {
    document.querySelector('#loaderpage').classList.add("hidden")
    document.querySelector('header').classList.remove("hidden")
    document.querySelector('main').classList.remove("hidden")
    document.querySelector('footer').classList.remove("hidden")
    window.onclick = function (event) {
        if (!event.target.closest('#menu-button') && !event.target.closest('#menu-button *')) {
            const dropdowns = document.getElementsByClassName('dropdown-content');
            for (let i = 0; i < dropdowns.length; i++) {
                const openDropdown = dropdowns[i];
                if (!openDropdown.classList.contains('hidden')) {
                    openDropdown.classList.add('hidden');
                }
            }
        }
    }
    setInterval(() => {
        // 
        let height = 400
        if (window.location.href == window.location.origin+"/") {
            height = 20
        }
        let classess = "fixed w-screen bg-indigo-200"
        let classlist = classess.split(" ")
        const scrolling = document.querySelector("#scrolling");
        if (window.scrollY > height) {
            classlist.forEach(element => {
                document.querySelector('header').classList.add(element)
                // document.querySelector('main').classList.add("py-96")
            });
            scrolling.classList.remove("hidden");
        } else {
            classlist.forEach(element => {
                // document.querySelector('main').classList.remove("py-96")
                document.querySelector('header').classList.remove(element)
            });
            scrolling.classList.add("hidden");
        }


    }, 1000)

    scrolling.addEventListener("click", (e) => {
        window.scrollTo(0, 0)
    });


    function shareToSocialMedia(platform, url) {
        let shareUrl = '';
        const encodedUrl = encodeURIComponent(url);

        switch (platform) {
            case 'facebook':
                shareUrl = `https://www.facebook.com/sharer/sharer.php?u=${encodedUrl}`;
                break;
            case 'twitter':
                shareUrl = `https://twitter.com/intent/tweet?url=${encodedUrl}`;
                break;
            case 'linkedin':
                shareUrl = `https://www.linkedin.com/sharing/share-offsite/?url=${encodedUrl}`;
                break;
            case 'whatsapp':
                shareUrl = `https://api.whatsapp.com/send?text=${encodedUrl}`;
                break;
            default:
                break;
        }

        if (shareUrl) {
            window.open(shareUrl, '_blank', 'width=600,height=400');
        }
    }
    const shareButtons = document.querySelectorAll('.share-button');
    shareButtons.forEach(button => {
        button.addEventListener('click', function (event) {
            event.preventDefault();
            const platform = this.dataset.platform;
            // const url = this.dataset.url;
            url = window.location.href;
            shareToSocialMedia(platform, url);
        });
    });

};