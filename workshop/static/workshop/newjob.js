document.addEventListener("DOMContentLoaded", function() {
    const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

    cutf = document.getElementById("id_cut")
    cutf.addEventListener("change", handleCutChange)


    function handleCutChange() {
        const selectedCutId = cutf.value;
        
        fetch(`http://127.0.0.1:8000/workshop/api/newjob_sizes/${selectedCutId}`, {
            method: 'GET',
            headers: {
              'Content-Type': 'application/json',
              'X-CSRFToken': csrfToken,
            }})
        .then(Response => Response.json())
        .then(data => {
        const idSizeElement = document.getElementById('id_size');
        idSizeElement.innerHTML = '';
        data.sizes.forEach(size => {
            const option = document.createElement('option');
            option.value = size.id;
            option.text = size.size;
            idSizeElement.appendChild(option);
        });
        sizef.dispatchEvent(new Event('change'));
        })
        .catch(error => console.error(error));
    }




    sizef = document.getElementById("id_size")
    sizef.addEventListener("change", handleSizeChange)

    function handleSizeChange() {
        const selectedSizeId = sizef.value;

        fetch(`http://127.0.0.1:8000/workshop/api/newjob_colors/${selectedSizeId}`, {
            method: 'GET',
            headers: {
              'Content-Type': 'application/json',
              'X-CSRFToken': csrfToken,
            }})
            .then(Response => Response.json())
            .then(data => {
            const idColorElement = document.getElementById('id_color');
            idColorElement.innerHTML = '';
            data.colors.forEach(color => {
                const option = document.createElement('option');
                option.value = color.id;
                option.text = color.color;
                idColorElement.appendChild(option);
            });
            colorf.dispatchEvent(new Event('change'));
            })
            .catch(error => console.error(error));
    }


    colorf = document.getElementById("id_color")
    colorf.addEventListener("change", handleColorChange)

    function handleColorChange() {
        const selectedColorId = colorf.value;

        fetch(`http://127.0.0.1:8000/workshop/api/newjob_lines/${selectedColorId}`, {
            method: 'GET',
            headers: {
              'Content-Type': 'application/json',
              'X-CSRFToken': csrfToken,
            },})
            .then(Response => Response.json())
            .then(data => {
            const idLineElement = document.getElementById('id_line');
            idLineElement.innerHTML = '';
            data.lines.forEach(line => {
                const option = document.createElement('option');
                option.value = line.id;
                option.text = line.line;
                idLineElement.appendChild(option);
            });
            })
            .catch(error => console.error(error));
    }
});
