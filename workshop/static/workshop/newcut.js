// Gets ID(s) of input field(s), toggles the list of attribute(s) given for that field. set the attribute(s) according to your needs as the second arg.
//both args should be arrays.
function toggleAttributef(inputids, attr) {
  for (let i = 0; i < inputids.length; i++) {
    let input = document.getElementById(inputids[i]);
    for (let j = 0; j < attr.length; j++) {
      let state = input.getAttribute(attr[j]);
      if (state === "") {
        input.removeAttribute(attr[j]);
      } else {
        input.setAttribute(attr[j], "");
        input.value = "";
      }
    }
  }
}

// To keep track of the number of sizes
let sizeCounter = 0;
// Everytime a size checkbox is checked, it creates a price input for that size. and everytime it's unchecked, the price input will be removed.
function sizeInputf(checkboxid) {
  let checkboxf = document.getElementById(checkboxid);
  let totalFormsf = document.getElementById("id_sizes-TOTAL_FORMS")
  let cardbody = document.getElementById("sizecardbody");
  let SizeInputId = `id_sizes-${totalFormsf.value}-size`;
  let amountInputId = `id_sizes-${totalFormsf.value}-amount`;

  if (checkboxf.checked) {
    // Creating parent DIV
    const newdiv = document.createElement("div");
    newdiv.classList.add("d-flex", "justify-content-center", "mt-3", "sizeparent");
    newdiv.id = `${checkboxf.id}_parent`;
    cardbody.appendChild(newdiv);
    //Creating hidden input for size type
    const newSizeInput = document.createElement("input");
    newSizeInput.id = SizeInputId;
    newSizeInput.name = `sizes-${totalFormsf.value}-size`;
    newSizeInput.type = "text";
    newSizeInput.value = checkboxf.id.toUpperCase();
    newSizeInput.required = true;
    newSizeInput.hidden = true;
    newdiv.appendChild(newSizeInput);
    // Creating amount input for the size type
    const newAmountInput = document.createElement("input");
    newAmountInput.classList.add("form-control", "form-control-sm", "sizeamount");
    newAmountInput.id = amountInputId;
    newAmountInput.name = `sizes-${totalFormsf.value}-amount`;
    newAmountInput.type = "number";
    newAmountInput.step = "1";
    newAmountInput.min = "1";
    newAmountInput.required = true;
    newAmountInput.placeholder = `${checkboxf.id.toUpperCase()} تعداد`;
    newAmountInput.setAttribute("style", "width: 250px;");
    newdiv.appendChild(newAmountInput);
    
    totalFormsf.value = parseInt(totalFormsf.value) + 1;
    sizeCounter++;
  }
  else {
    let parentToRemovef = document.getElementById(`${checkboxf.id}_parent`)
    if (parentToRemovef) {
      parentToRemovef.remove();
      totalFormsf.value = parseInt(totalFormsf.value) - 1;
      sizeCounter--;
    }
  }

  let totalsizes = document.getElementById("totalsizes");
  totalsizes.innerText = sizeCounter;
}


// To keep track of the number of colors
let colorCounter = 0;

// Creates a new color input 
function addColor() {
  // Get the colorcardbody element
  const cardBody = document.getElementById("colorcardbody");
  // Get the management form counter
  const totalColorForms = document.getElementById("id_colors-TOTAL_FORMS");

  // Create a new colorrow div
  const newColorRow = document.createElement("div");
  newColorRow.classList.add("d-flex", "justify-content-center", "color-body-child");

  // Create the first column for color name input
  const col1 = document.createElement("div");
  col1.classList.add("col-md-7", "mt-2", "ms-2");
  const colorNameInput = document.createElement("input");
  colorNameInput.type = "text";
  colorNameInput.id = `id_colors-${totalColorForms.value}-color`;
  colorNameInput.name = `colors-${totalColorForms.value}-color`;
  colorNameInput.placeholder = "نام رنگ";
  colorNameInput.classList.add("form-control", "form-control-sm");
  colorNameInput.required = true;
  col1.appendChild(colorNameInput);


  // Create the third column for color amount input
  const col3 = document.createElement("div");
  col3.classList.add("col-md-2", "mt-2");
  const colorAmountInput = document.createElement("input");
  colorAmountInput.type = "number";
  colorAmountInput.min = "1";
  colorAmountInput.step = "1";
  colorAmountInput.id = `id_colors-${totalColorForms.value}-amount`;
  colorAmountInput.name = `colors-${totalColorForms.value}-amount`;
  colorAmountInput.placeholder = "تعداد";
  colorAmountInput.classList.add("form-control", "form-control-sm", "coloramount", "mx-1");
  colorAmountInput.required = true;
  col3.appendChild(colorAmountInput);

  // Create the fourth column for the close button
  const col4 = document.createElement("div");
  col4.classList.add("col-md-1", "d-flex", "align-items-center");
  const closeButton = document.createElement("button");
  closeButton.type = "button";
  closeButton.classList.add("btn", "btn-sm", "btn-outline-primary", "mx-2");
  closeButton.innerHTML = "X";
  closeButton.addEventListener("click", function() {
    newColorRow.remove();
    updateTotalColors();
  });
  col4.appendChild(closeButton);

  // Append the columns to the colorrow
  newColorRow.appendChild(col1);
  newColorRow.appendChild(col3);
  newColorRow.appendChild(col4);

  // Append the new colorrow to the colorcardbody element
  cardBody.appendChild(newColorRow);

  // Increment the color counter
  totalColorForms.value = parseInt(totalColorForms.value) + 1;
  colorCounter++;

  // Update the total number of colors
  updateTotalColors();

  function updateTotalColors() {
    const totalColors = document.getElementById("totalcolors");
    const rows = document.querySelectorAll("#colorcardbody > div");
    totalColors.textContent = rows.length.toString();
    totalColorForms.value = rows.length.toString();
  }
}



// To keep track of the number of lines
let lineCounter = 0;

// Creates a new line input 
function addLine() {
  // Get the linecardbody element
  const cardBody = document.getElementById("linecardbody");
  // Get the management form counter
  const totalLinesForms = document.getElementById("id_lines-TOTAL_FORMS");

  // Create a new linerow div
  const newLineRow = document.createElement("div");
  newLineRow.classList.add("d-flex", "justify-content-center", "color-body-child");

  // Create the column for line name input
  const col1 = document.createElement("div");
  col1.classList.add("col-md-7", "mt-2", "ms-2");
  const colorNameInput = document.createElement("input");
  colorNameInput.type = "text";
  colorNameInput.id = `id_lines-${totalLinesForms.value}-line`;
  colorNameInput.name = `lines-${totalLinesForms.value}-line`;
  colorNameInput.placeholder = "نام خط";
  colorNameInput.classList.add("form-control", "form-control-sm");
  colorNameInput.required = true;
  col1.appendChild(colorNameInput);


  // Create the column for the close button
  const col2 = document.createElement("div");
  col2.classList.add("col-md-1", "d-flex", "align-items-center");
  const closeButton = document.createElement("button");
  closeButton.type = "button";
  closeButton.classList.add("btn", "btn-sm", "btn-outline-primary", "mx-1");
  closeButton.innerHTML = "X";
  closeButton.addEventListener("click", function() {
    newLineRow.remove();
    updateTotalLines();
  });
  col2.appendChild(closeButton);

  // Append the columns to the line row
  newLineRow.appendChild(col1);
  newLineRow.appendChild(col2);

  // Append the new line row to the linecardbody element
  cardBody.appendChild(newLineRow);

  // Increment the line counter
  totalLinesForms.value = parseInt(totalLinesForms.value) + 1;
  lineCounter++;

  // Update the total number of lines
  updateTotalLines();

  function updateTotalLines() {
    const totalLines = document.getElementById("totallines");
    const rows = document.querySelectorAll("#linecardbody > div");
    totalLines.textContent = rows.length.toString();
    totalLinesForms.value = rows.length.toString();
  }
}


function radiotogglef() {
  let whitef = document.getElementById("id_colortype_0");
  let colorfulf = document.getElementById("id_colortype_1");
  let printedf = document.getElementById("id_colortype_2");
  let addcolorf = document.getElementById("newcolorbtn");
  let colorcounter = document.getElementById("totalcolors");
  let cardBody = document.getElementById("colorcardbody");

  whitef.addEventListener("click", function() {
    if (whitef.checked) {
      addcolorf.setAttribute("disabled", "true")
      colorcounter.innerText = 1;
      while (cardBody.firstChild) {
        cardBody.removeChild(cardBody.firstChild);
      }
    }
    else {
      addcolorf.removeAttribute("disabled")
    }
  });

  colorfulf.addEventListener("click", function() {
    if (addcolorf.disabled) {
      addcolorf.removeAttribute("disabled")
      colorcounter.innerText = 0;
    }
  });

  printedf.addEventListener("click", function() {
    if (addcolorf.disabled) {
      addcolorf.removeAttribute("disabled")
      colorcounter.innerText = 0;
    }
  });
}



function loadedPage() {
  document.addEventListener("DOMContentLoaded", function() {
    // Function of the sizes radio buttons and affiliated functionalities
    const totalSizes = document.getElementById('totalsizes');
    const totalFormsf = document.getElementById("id_sizes-TOTAL_FORMS")

    const youngRadiof = document.getElementById('id_sizetype_1');
    youngRadiof.addEventListener('click', function () {
        totalSizes.innerText = 0;
        totalFormsf.value = 0;
        sizeCounter = 0;

        let sizeParentElementsf = document.getElementsByClassName('sizeparent');
        let youngParentElementsf = document.getElementsByClassName('youngparent');
        let adultParentElementsf = document.getElementsByClassName('adultparent');
        let adultElementsf = document.getElementsByClassName('adult');
        console.log(sizeParentElementsf.length)

        for (var i = 0; i < adultParentElementsf.length; i++) {
          adultElementsf[i].checked = false;
          adultParentElementsf[i].setAttribute('style', 'display:none !important');
        };

        for (var i = 0; i < youngParentElementsf.length; i++) {
          youngParentElementsf[i].removeAttribute('style');
        };

        for (var i = sizeParentElementsf.length - 1; i >= 0; i--) {
          console.log(sizeParentElementsf.length)
          sizeParentElementsf[i].remove();
        };
    });

    const adultRadiof = document.getElementById('id_sizetype_0');
    adultRadiof.addEventListener('click', function () {
      totalSizes.innerText = 0;
      totalFormsf.value = 0;
      sizeCounter = 0;

      let sizeParentElementsf = document.getElementsByClassName('sizeparent');
      let youngParentElementsf = document.getElementsByClassName('youngparent');
      let adultParentElementsf = document.getElementsByClassName('adultparent');
      let youngElementsf = document.getElementsByClassName('young');

      for (var i = 0; i < youngParentElementsf.length; i++) {
        youngElementsf[i].checked = false;
        youngElementsf[i].parentNode.setAttribute('style', 'display:none !important');
      };

      for (var i = 0; i < adultParentElementsf.length; i++) {
        adultParentElementsf[i].removeAttribute('style');
      };

      for (var i = sizeParentElementsf.length - 1; i >= 0; i--) {
        sizeParentElementsf[i].remove();
      };

      totalFormsf.value = 0;
    });


    // Showing and hiding error for "No color is added"
    const colorcheckboxerrorf = document.getElementById("colorcheckboxerror");
    const colornumf = document.getElementById("totalcolors");
    const colorobserver = new MutationObserver(function(mutations) {
      mutations.forEach((mutation) => {
        if (mutation.type === 'childList' || mutation.type === 'characterData') {
          const totalColors = parseInt(colornumf.innerText);
          if (totalColors > 0) {
            colorcheckboxerrorf.removeAttribute('required');
          } else {
            colorcheckboxerrorf.setAttribute('required', 'true');
          }
        }
      })
    });
    colorobserver.observe(colornumf, { childList: true, characterData: true, subtree: true });


    // Showing and hiding error for "No size is selected"
    const sizecheckboxerrorf = document.getElementById("sizecheckboxerror");
    const sizenumf = document.getElementById("totalsizes");
    const sizeobserver = new MutationObserver(function(mutations) {
      mutations.forEach((mutation) => {
        if (mutation.type === 'childList' && mutation.target === sizenumf) {
          const totalSizes = parseInt(sizenumf.innerText);
          if (totalSizes > 0) {
            sizecheckboxerrorf.removeAttribute('required');
          } else {
            sizecheckboxerrorf.setAttribute('required', 'true');
          }
        }
      })
    });
    sizeobserver.observe(sizenumf, { childList: true, characterData: true, subtree: true });


    // Showing and hiding error for "No line is selected"
    const linecheckboxerrorf = document.getElementById("linecheckboxerror");
    const linenumf = document.getElementById("totallines");
    const lineobserver = new MutationObserver(function(mutations) {
      mutations.forEach((mutation) => {
        if (mutation.type === 'childList' && mutation.target === linenumf) {
          const totalLines = parseInt(linenumf.innerText);
          if (totalLines > 0) {
            linecheckboxerrorf.removeAttribute('required');
          } else {
            linecheckboxerrorf.setAttribute('required', 'true');
          }
        }
      })
    });
    lineobserver.observe(linenumf, { childList: true, characterData: true, subtree: true });


    // For comparing total of colors and total of sizes
    let colorAmountElements;
    let colorAmountListf = {};
    let colorTotalf = 0;
    let sizeAmountElements;
    let sizeAmountListf = {};
    let sizeTotalf = 0;

    // Observer for colorcardbody children
    let colorBodyElement = document.getElementById("colorcardbody");
    const colorBodyObserver = new MutationObserver(entries => {
      colorAmountElements = document.querySelectorAll(".coloramount");
      counter = 0;
      colorAmountElements.forEach((element) => {
        element.addEventListener('input', (event) => {
          colorAmountListf[element.id] = (parseInt(element.value));
          colorTotalf = parseInt(Object.values(colorAmountListf).reduce((acc, curr) => acc + curr, 0));

          equalityerrorf = document.getElementById("equalityerror");
          if (sizeTotalf === colorTotalf) {
            equalityerrorf.removeAttribute('required');
          }
          else {
            equalityerrorf.setAttribute('required', 'true');
          }
        });
        counter++;
      });
    });
    colorBodyObserver.observe(colorBodyElement, { subtree: true, childList: true, attributes: true });


    // Observer for sizecardbody children
    sizeBodyElement = document.getElementById("sizecardbody");
    const sizeBodyObserver = new MutationObserver(entries => {
      sizeAmountElements = document.querySelectorAll(".sizeamount");
      counter = 0;
      sizeAmountElements.forEach((element) => {
        element.addEventListener('input', (event) => {
          sizeAmountListf[element.id] = (parseInt(element.value));
          sizeTotalf = parseInt(Object.values(sizeAmountListf).reduce((acc, curr) => acc + curr, 0));
          equalityerrorf = document.getElementById("equalityerror");
          if (colorTotalf === sizeTotalf) {
            equalityerrorf.removeAttribute('required');
          }
          else {
            equalityerrorf.setAttribute('required', 'true');
          }
        });
        counter++;
      });
    });
    sizeBodyObserver.observe(sizeBodyElement, { subtree: true, childList: true, attributes: true });
  });
}




  function finalvalidationf(event) {
    let mainform = document.getElementById('mainform');
    if (!mainform.checkValidity()) {
      event.preventDefault();
      event.stopPropagation();
      var firstInvalidInput = document.querySelector(".form-control:invalid");
      if (firstInvalidInput) {
        firstInvalidInput.scrollIntoView({ behavior: "smooth", block: "center" });
      }
      else {
        mainform.submit();
      }
    }
    mainform.classList.add('was-validated');
  }