/**
 * ============================================================================
 * PORTFOLIO JAVASCRIPT
 * Developer: A.P. Annie Nimisha
 * Role: Full Stack Developer & CSE Student
 * Features: Typewriter, Smooth Scroll, Mobile Drawer, Form Validation,
 *           Scroll Spy, Modal Dialogs & Toast Notifications
 * ============================================================================
 */

document.addEventListener('DOMContentLoaded', () => {
  // --------------------------------------------------------------------------
  // 1. DYNAMIC COPYRIGHT YEAR
  // --------------------------------------------------------------------------
  const currentYearSpan = document.getElementById('currentYear');
  if (currentYearSpan) {
    currentYearSpan.textContent = new Date().getFullYear();
  }

  // --------------------------------------------------------------------------
  // 2. HERO TYPEWRITER ANIMATION
  // --------------------------------------------------------------------------
  const typewriterElement = document.getElementById('typewriterText');
  const phrases = [
    'Full Stack Developer',
    'B.E. CSE Student • 9.2 CGPA',
    'DMI Engineering College (2024–2028)',
    'Ideathon 2nd Prize Winner',
    'AI & Web Solutions Builder'
  ];

  let phraseIndex = 0;
  let charIndex = 0;
  let isDeleting = false;
  let typingSpeed = 90;

  function typeWriter() {
    if (!typewriterElement) return;

    const currentPhrase = phrases[phraseIndex];

    if (isDeleting) {
      typewriterElement.textContent = currentPhrase.substring(0, charIndex - 1);
      charIndex--;
      typingSpeed = 45;
    } else {
      typewriterElement.textContent = currentPhrase.substring(0, charIndex + 1);
      charIndex++;
      typingSpeed = 100;
    }

    if (!isDeleting && charIndex === currentPhrase.length) {
      // Pause at the end of the phrase
      typingSpeed = 1800;
      isDeleting = true;
    } else if (isDeleting && charIndex === 0) {
      // Move to next phrase
      isDeleting = false;
      phraseIndex = (phraseIndex + 1) % phrases.length;
      typingSpeed = 500;
    }

    setTimeout(typeWriter, typingSpeed);
  }

  typeWriter();

  // --------------------------------------------------------------------------
  // 3. NAVBAR SCROLL EFFECT & MOBILE DRAWER
  // --------------------------------------------------------------------------
  const navbar = document.getElementById('navbar');
  const hamburger = document.getElementById('hamburger');
  const navMenu = document.getElementById('navMenu');
  const navLinks = document.querySelectorAll('.nav-link');

  // Change navbar appearance on scroll
  window.addEventListener('scroll', () => {
    if (window.scrollY > 40) {
      navbar?.classList.add('scrolled');
    } else {
      navbar?.classList.remove('scrolled');
    }
  });

  // Toggle mobile drawer
  if (hamburger && navMenu) {
    hamburger.addEventListener('click', () => {
      const isOpen = navMenu.classList.toggle('open');
      hamburger.classList.toggle('active');
      hamburger.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });

    // Close mobile drawer when clicking any nav link
    navLinks.forEach(link => {
      link.addEventListener('click', () => {
        navMenu.classList.remove('open');
        hamburger.classList.remove('active');
        hamburger.setAttribute('aria-expanded', 'false');
      });
    });

    // Close when clicking outside menu
    document.addEventListener('click', (e) => {
      if (!navMenu.contains(e.target) && !hamburger.contains(e.target) && navMenu.classList.contains('open')) {
        navMenu.classList.remove('open');
        hamburger.classList.remove('active');
        hamburger.setAttribute('aria-expanded', 'false');
      }
    });

    // Close on Escape key
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && navMenu.classList.contains('open')) {
        navMenu.classList.remove('open');
        hamburger.classList.remove('active');
        hamburger.setAttribute('aria-expanded', 'false');
      }
    });
  }

  // --------------------------------------------------------------------------
  // 4. ACTIVE NAVIGATION LINK (SCROLL SPY)
  // --------------------------------------------------------------------------
  const sections = document.querySelectorAll('section[id]');

  function updateActiveNavLink() {
    const scrollY = window.pageYOffset;

    sections.forEach(current => {
      const sectionHeight = current.offsetHeight;
      const sectionTop = current.offsetTop - 120;
      const sectionId = current.getAttribute('id');
      const matchingLink = document.querySelector(`.nav-link[href*="${sectionId}"]`);

      if (matchingLink) {
        if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
          matchingLink.classList.add('active');
        } else {
          matchingLink.classList.remove('active');
        }
      }
    });
  }

  window.addEventListener('scroll', updateActiveNavLink);

  // --------------------------------------------------------------------------
  // 5. SCROLL REVEAL ANIMATIONS (INTERSECTION OBSERVER)
  // --------------------------------------------------------------------------
  const animatedElements = document.querySelectorAll('.animate-fade, .card-glass');

  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries, obs) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('in-view');
          obs.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.12,
      rootMargin: '0px 0px -40px 0px'
    });

    animatedElements.forEach(el => observer.observe(el));
  } else {
    // Fallback for older browsers
    animatedElements.forEach(el => el.classList.add('in-view'));
  }

  // --------------------------------------------------------------------------
  // 6. BACK TO TOP BUTTON
  // --------------------------------------------------------------------------
  const backToTopBtn = document.getElementById('backToTopBtn');

  if (backToTopBtn) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 350) {
        backToTopBtn.classList.add('visible');
      } else {
        backToTopBtn.classList.remove('visible');
      }
    });

    backToTopBtn.addEventListener('click', () => {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  }

  // --------------------------------------------------------------------------
  // 7. TOAST NOTIFICATION UTILITY
  // --------------------------------------------------------------------------
  const toast = document.getElementById('toastNotification');
  const toastMessage = document.getElementById('toastMessage');
  const toastIcon = document.getElementById('toastIcon');
  let toastTimeout;

  function showToast(message, iconClass = 'fa-solid fa-circle-check', duration = 3500) {
    if (!toast || !toastMessage) return;

    clearTimeout(toastTimeout);
    toastMessage.textContent = message;
    if (toastIcon) {
      toastIcon.className = `${iconClass} toast-icon`;
    }

    toast.classList.add('show');

    toastTimeout = setTimeout(() => {
      toast.classList.remove('show');
    }, duration);
  }

  // --------------------------------------------------------------------------
  // 8. COPY EMAIL & PHONE BUTTONS
  // --------------------------------------------------------------------------
  const copyEmailBtn = document.getElementById('copyEmailBtn');
  const emailToCopy = 'annienimisha2006@gmail.com';

  if (copyEmailBtn) {
    copyEmailBtn.addEventListener('click', () => {
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(emailToCopy)
          .then(() => {
            showToast('Email copied to clipboard: ' + emailToCopy);
          })
          .catch(() => {
            fallbackCopy(emailToCopy);
          });
      } else {
        fallbackCopy(emailToCopy);
      }
    });
  }

  const copyPhoneBtn = document.getElementById('copyPhoneBtn');
  const phoneToCopy = '+919597515781';

  if (copyPhoneBtn) {
    copyPhoneBtn.addEventListener('click', () => {
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(phoneToCopy)
          .then(() => {
            showToast('Phone number copied to clipboard: +91 9597515781', 'fa-solid fa-phone');
          })
          .catch(() => {
            fallbackCopy(phoneToCopy);
          });
      } else {
        fallbackCopy(phoneToCopy);
      }
    });
  }

  // --------------------------------------------------------------------------
  // 8B. INTERACTIVE RESUME PAGE SWITCHER
  // --------------------------------------------------------------------------
  const resumeTab1 = document.getElementById('resumeTab1');
  const resumeTab2 = document.getElementById('resumeTab2');
  const resumePageImg = document.getElementById('resumePageImg');

  if (resumeTab1 && resumeTab2 && resumePageImg) {
    resumeTab1.addEventListener('click', () => {
      resumeTab1.classList.add('active');
      resumeTab2.classList.remove('active');
      resumePageImg.style.opacity = '0.3';
      setTimeout(() => {
        resumePageImg.src = 'assets/resume/resume_page_1.png';
        resumePageImg.alt = 'A P Annie Nimisha Resume - Page 1';
        resumePageImg.style.opacity = '1';
      }, 150);
    });

    resumeTab2.addEventListener('click', () => {
      resumeTab2.classList.add('active');
      resumeTab1.classList.remove('active');
      resumePageImg.style.opacity = '0.3';
      setTimeout(() => {
        resumePageImg.src = 'assets/resume/resume_page_2.png';
        resumePageImg.alt = 'A P Annie Nimisha Resume - Page 2';
        resumePageImg.style.opacity = '1';
      }, 150);
    });
  }

  // Modal trigger for full resume preview
  const viewResumeModalBtn = document.getElementById('viewResumeModalBtn');
  const heroViewResumeBtn = document.getElementById('heroViewResumeBtn');
  
  function openResumePreviewModal() {
    openModal(
      'Curriculum Vitae — A P Annie Nimisha',
      `<div style="text-align: center;">
        <p style="margin-bottom: 16px; color: var(--text-secondary);">
          Review the complete official 2-page resume or download the PDF document below.
        </p>
        <div style="display: flex; justify-content: center; gap: 12px; margin-bottom: 20px; flex-wrap: wrap;">
          <a href="assets/resume/resume.pdf" class="btn btn-primary btn-sm" download="A_P_Annie_Nimisha_Resume.pdf">
            <i class="fa-solid fa-download"></i> Download PDF
          </a>
          <a href="assets/resume/resume.pdf" target="_blank" rel="noopener noreferrer" class="btn btn-outline btn-sm">
            <i class="fa-solid fa-arrow-up-right-from-square"></i> Open in New Tab
          </a>
        </div>
        <div style="display: flex; flex-direction: column; gap: 18px; max-height: 60vh; overflow-y: auto; padding: 8px;">
          <img src="assets/resume/resume_page_1.png" alt="A P Annie Nimisha Resume Page 1" style="width: 100%; border-radius: 6px; box-shadow: 0 4px 20px rgba(0,0,0,0.4);" />
          <img src="assets/resume/resume_page_2.png" alt="A P Annie Nimisha Resume Page 2" style="width: 100%; border-radius: 6px; box-shadow: 0 4px 20px rgba(0,0,0,0.4);" />
        </div>
      </div>`,
      'fa-solid fa-file-invoice'
    );
  }

  if (viewResumeModalBtn) viewResumeModalBtn.addEventListener('click', openResumePreviewModal);
  if (heroViewResumeBtn) heroViewResumeBtn.addEventListener('click', openResumePreviewModal);

  // Attach modal trigger to Certification "Verify" buttons
  const certButtons = document.querySelectorAll('.cert-verify-btn');
  const certDetailsMap = {
    'Swayam NPTEL': 'Python Programming certification offered by Swayam NPTEL covering structured programming, data structures, and algorithms.',
    'Novi Tech': 'Data Analytics Certificate Course in Python (CCP) covering exploratory data analysis, data manipulation, and visualization.',
    'MongoDB': 'MongoDB Basics for Students covering document schemas, collections, queries, and NoSQL architecture.',
    'CSC': 'Python course completed at CSC focusing on core scripting, syntax, and object-oriented paradigms.',
    'CS50': 'Currently pursuing Harvard University’s CS50x (Introduction to Computer Science), covering C, memory management, algorithms, Python, SQL, and web technologies.'
  };

  certButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const certName = btn.getAttribute('data-cert') || 'Course';
      const detail = certDetailsMap[certName] || `Official certification record for <strong>${certName}</strong>.`;
      openModal(
        `${certName} — Certificate`,
        `${detail}<br><br>
        <span style="font-size: 0.88rem; color: var(--text-muted);"><i class="fa-solid fa-shield-halved"></i> Verified credential / ongoing course in Annie's professional portfolio.</span>`,
        'fa-solid fa-certificate'
      );
    });
  });

  // --------------------------------------------------------------------------
  // 10. PROFESSIONAL CONTACT FORM (CLIENT-SIDE VALIDATION)
  // --------------------------------------------------------------------------
  const contactForm = document.getElementById('contactForm');
  const nameInput = document.getElementById('contactName');
  const emailInput = document.getElementById('contactEmail');
  const messageInput = document.getElementById('contactMessage');

  const nameError = document.getElementById('nameError');
  const emailError = document.getElementById('emailError');
  const messageError = document.getElementById('messageError');
  const submitBtn = document.getElementById('submitFormBtn');

  function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(String(email).toLowerCase());
  }

  function clearErrors() {
    if (nameError) nameError.textContent = '';
    if (emailError) emailError.textContent = '';
    if (messageError) messageError.textContent = '';

    nameInput?.classList.remove('input-error');
    emailInput?.classList.remove('input-error');
    messageInput?.classList.remove('input-error');
  }

  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      clearErrors();

      let isValid = true;

      // Validate Name
      const nameVal = nameInput ? nameInput.value.trim() : '';
      if (!nameVal) {
        if (nameError) nameError.textContent = 'Please enter your name.';
        nameInput?.classList.add('input-error');
        isValid = false;
      }

      // Validate Email
      const emailVal = emailInput ? emailInput.value.trim() : '';
      if (!emailVal) {
        if (emailError) emailError.textContent = 'Please enter your email address.';
        emailInput?.classList.add('input-error');
        isValid = false;
      } else if (!validateEmail(emailVal)) {
        if (emailError) emailError.textContent = 'Please enter a valid email address.';
        emailInput?.classList.add('input-error');
        isValid = false;
      }

      // Validate Message
      const messageVal = messageInput ? messageInput.value.trim() : '';
      if (!messageVal) {
        if (messageError) messageError.textContent = 'Please enter your message.';
        messageInput?.classList.add('input-error');
        isValid = false;
      } else if (messageVal.length < 10) {
        if (messageError) messageError.textContent = 'Message should be at least 10 characters.';
        messageInput?.classList.add('input-error');
        isValid = false;
      }

      if (!isValid) return;

      // Simulate sending state
      const originalBtnHTML = submitBtn ? submitBtn.innerHTML : '';
      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Validating...';
      }

      setTimeout(() => {
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.innerHTML = originalBtnHTML;
        }

        // Inform the user honestly about front-end status and direct email options
        openModal(
          'Message Validated Successfully! ✨',
          `Hello <strong>${nameVal}</strong>,<br><br>
          Thank you for reaching out! Your message details have been validated by the frontend.<br><br>
          <em>Note:</em> To send an actual email directly to <strong>annienimisha2006@gmail.com</strong> right now, you can click on the direct email link in the contact card, or follow the Formspree / EmailJS guide in <code>README.md</code> to activate live form delivery in 2 minutes!`,
          'fa-solid fa-paper-plane'
        );

        // Reset form inputs
        contactForm.reset();
      }, 700);
    });
  }
});
