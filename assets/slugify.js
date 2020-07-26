const titleInput = document.querySelector('input[name=title]')
const slugInput = document.querySelector('input[name=slug]')

const slugify = (val)=>{
  return val.toString().trim()
    .replace(/&/g,'-and-')    //replace & with -and-
    .replace(/[\s\W-]+/g,'-')
};

titleInput.addEventListener('keyup',(e)=>{
  slugInput.setAttribute('value',slugify(titleInput.value));
});
