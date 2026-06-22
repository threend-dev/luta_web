// ===== LUTA Web - SPA Router & Interactions =====

let featuresScrollListenerAdded = false;

document.addEventListener('DOMContentLoaded', () => {
  initRouter();
  initMobileNav();
  initLightbox();
});

// ===== SPA Router =====
function initRouter() {
  // 이벤트 위임: 동적으로 로드된 콘텐츠의 링크도 처리
  document.addEventListener('click', (e) => {
    const link = e.target.closest('[data-page]');
    if (link) {
      e.preventDefault();
      navigateTo(link.getAttribute('data-page'));
    }
  });

  // Handle browser back/forward
  window.addEventListener('popstate', (e) => {
    const page = e.state?.page || 'home';
    showPage(page, false);
  });

  // Initial page from URL hash
  const initialPage = window.location.hash.replace('#', '') || 'home';
  showPage(initialPage, false);
}

function navigateTo(page) {
  showPage(page, true);
}

async function showPage(pageId, pushState = true) {
  const navLinks = document.querySelectorAll('.nav-link');

  // Update nav active state
  navLinks.forEach(link => {
    link.classList.remove('active');
    if (link.getAttribute('data-page') === pageId) {
      link.classList.add('active');
    }
  });

  // Update URL
  if (pushState) {
    history.pushState({ page: pageId }, '', `#${pageId}`);
  }

  // Load page content
  const target = document.getElementById(`page-${pageId}`);
  if (target) {
    try {
      const res = await fetch(`views/${pageId}.html`, { cache: 'no-cache' });
      if (!res.ok) throw new Error(`페이지 로드 실패: ${pageId}`);
      target.innerHTML = await res.text();

      // 페이지별 기능 초기화
      if (pageId === 'faq') initFAQ();
      if (pageId === 'features') initFeaturesNav();
    } catch (err) {
      console.error(err);
    }
  }

  // Hide all pages, show target
  document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
  if (target) {
    target.classList.add('active');
  }

  // Scroll to top
  window.scrollTo({ top: 0, behavior: 'smooth' });

  // Close mobile menu
  closeMobileNav();
}

// ===== Mobile Navigation =====
function initMobileNav() {
  const toggle = document.getElementById('navToggle');
  const menu = document.getElementById('navMenu');

  toggle.addEventListener('click', () => {
    toggle.classList.toggle('active');
    menu.classList.toggle('active');
    document.body.classList.toggle('nav-open');
  });
}

function closeMobileNav() {
  const toggle = document.getElementById('navToggle');
  const menu = document.getElementById('navMenu');
  toggle.classList.remove('active');
  menu.classList.remove('active');
  document.body.classList.remove('nav-open');
}

// ===== FAQ Accordion =====
function initFAQ() {
  const faqItems = document.querySelectorAll('.faq-item');

  faqItems.forEach(item => {
    const question = item.querySelector('.faq-question');
    question.addEventListener('click', () => {
      const isOpen = item.classList.contains('open');

      // Close all
      faqItems.forEach(i => i.classList.remove('open'));

      // Toggle current
      if (!isOpen) {
        item.classList.add('open');
      }
    });
  });
}

// ===== Features Page Sidebar Navigation =====
function initFeaturesNav() {
  const featNavLinks = document.querySelectorAll('.features-nav-link');

  featNavLinks.forEach(link => {
    link.addEventListener('click', (e) => {
      e.preventDefault();
      const targetId = link.getAttribute('data-feat');
      const targetEl = document.getElementById(targetId);

      if (targetEl) {
        // Update active state
        featNavLinks.forEach(l => l.classList.remove('active'));
        link.classList.add('active');

        // Scroll to section
        const navbarHeight = document.getElementById('navbar').offsetHeight;
        const featNavHeight = document.querySelector('.features-nav-wrapper')?.offsetHeight || 0;
        const offset = navbarHeight + featNavHeight + 20;

        const top = targetEl.getBoundingClientRect().top + window.pageYOffset - offset;
        window.scrollTo({ top, behavior: 'smooth' });
      }
    });
  });

  // 스크롤 리스너는 최초 1회만 등록
  if (!featuresScrollListenerAdded) {
    featuresScrollListenerAdded = true;
    window.addEventListener('scroll', () => {
      const featuresPage = document.getElementById('page-features');
      if (!featuresPage?.classList.contains('active')) return;

      const sections = document.querySelectorAll('.feature-section');
      const navLinks = document.querySelectorAll('.features-nav-link');
      const navbarHeight = document.getElementById('navbar').offsetHeight;
      const featNavHeight = document.querySelector('.features-nav-wrapper')?.offsetHeight || 0;
      const offset = navbarHeight + featNavHeight + 100;

      let currentSection = '';
      sections.forEach(section => {
        const sectionTop = section.offsetTop - offset;
        if (window.pageYOffset >= sectionTop) {
          currentSection = section.getAttribute('id');
        }
      });

      navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('data-feat') === currentSection) {
          link.classList.add('active');
        }
      });
    });
  }
}

// ===== Navbar scroll effect =====
window.addEventListener('scroll', () => {
  const navbar = document.getElementById('navbar');
  if (window.scrollY > 50) {
    navbar.classList.add('scrolled');
  } else {
    navbar.classList.remove('scrolled');
  }
});

// ===== Lightbox =====
function initLightbox() {
  const lightbox = document.getElementById('lightbox');
  const lightboxImg = document.getElementById('lightbox-img');
  const closeBtn = document.querySelector('.lightbox-close');

  if (!lightbox) return;

  document.addEventListener('click', (e) => {
    if (e.target.tagName === 'IMG' && e.target.closest('.screenshot-item')) {
      lightboxImg.src = e.target.src;
      lightbox.classList.add('active');
    }
  });

  if (closeBtn) {
    closeBtn.addEventListener('click', () => {
      lightbox.classList.remove('active');
    });
  }

  lightbox.addEventListener('click', (e) => {
    if (e.target === lightbox) {
      lightbox.classList.remove('active');
    }
  });
}
