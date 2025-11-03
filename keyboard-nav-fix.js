// Add this function at end of init() function
function initKeyboardNavigation(){
    const dropdownItems=document.querySelectorAll('.dropdown-menu li');
    dropdownItems.forEach(item=>{
        if(item.style.pointerEvents==='none')return;
        item.setAttribute('tabindex','0');
        item.setAttribute('role','menuitem');
        item.addEventListener('keypress',(e)=>{
            if(e.key==='Enter'||e.key===' '){
                e.preventDefault();
                item.click();
            }
        });
        item.addEventListener('keydown',(e)=>{
            const items=Array.from(item.parentElement.querySelectorAll('li[tabindex="0"]'));
            const currentIndex=items.indexOf(item);
            if(e.key==='ArrowDown'){
                e.preventDefault();
                const nextIndex=(currentIndex+1)%items.length;
                items[nextIndex].focus();
            }else if(e.key==='ArrowUp'){
                e.preventDefault();
                const prevIndex=(currentIndex-1+items.length)%items.length;
                items[prevIndex].focus();
            }else if(e.key==='Escape'){
                e.preventDefault();
                const dropdown=item.closest('.has-dropdown');
                if(dropdown){
                    const trigger=dropdown.querySelector(':scope>:first-child');
                    if(trigger)trigger.focus();
                }
            }
        });
    });
    console.log('Keyboard navigation initialized for',dropdownItems.length,'dropdown items');
}
// Add initKeyboardNavigation(); call at the end of init() function
