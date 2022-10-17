const sideScroll = () => {
    const listWrapperElement = document.querySelector(".js-listWrapper");
    const listElement = document.querySelector(".js-list");
    const progressText = document.querySelector(".js-progressText");
    const progressLine = document.querySelector(".js-progressLine");
  
    gsap.to(listElement, {
      x: () => -(listElement.clientWidth - listWrapperElement.clientWidth),
      ease: "none",
      scrollTrigger: {
        trigger: ".js-section",
        start: "top top",
        end: () => `+=${listElement.clientWidth - listWrapperElement.clientWidth}`,
        scrub: true,
        pin: true,
        markers: true,
        anticipatePin: 1,
        invalidateOnRefresh: true,
        onUpdate: self => {
          progressText.textContent = `${Math.trunc((parseFloat(self.progress.toFixed(2))) * 100)}%`
          progressLine.style.width = `${Math.trunc((parseFloat(self.progress.toFixed(2))) * 100)}%`
        }
      }
    });
  }
  
  sideScroll();