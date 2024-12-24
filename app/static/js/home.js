// Define async function to fetch and display data
async function fetch_url(type, loadingElem_id, destElem_id) {
    // Display loading indicator
    document.getElementById(loadingElem_id).innerHTML = '<img class="size-12" src="../static/img/loading.gif" alt="Loading...">';

    try {
        const response = await fetch(`/get_url/${type}`, {
            method: "GET",
            headers: { 'Content-Type': 'application/json; charset=utf-8' }
        });

        if (!response.ok) {
            throw new Error(`Error: ${response.status} ${response.statusText}`);
        }

        const data = await response.json();

        // Log data for debugging
        console.log("Received data:", data);

        // Get the destination element
        const destElem = document.getElementById(destElem_id);

        // Clear any existing content in the destination element
        destElem.innerHTML = "";

        // Iterate over the list of URLs and create HTML elements
        data.urls.forEach((url, index) => {
            destElem.innerHTML += `<div class="h-10 border-b mb-1 flex relative">
          <span id="link-${index}" class="ml-1 inline-block w-[40%] overflow-hidden overflow-ellipsis rounded-md rounded-r-none place-content-center even:bg-gray-100">
            ${url}
          </span>
          
          <!-- Copy Icon -->
          <button onclick="copyText(\`link-${index}\`)" class="flex-none rounded-md rounded-l-none w-11 h-10 my-auto bg-[#3b83f6fb]">

            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6 stroke-white mx-auto">
              <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 17.25v3.375c0 .621-.504 1.125-1.125 1.125h-9.75a1.125 1.125 0 0 1-1.125-1.125V7.875c0-.621.504-1.125 1.125-1.125H6.75a9.06 9.06 0 0 1 1.5.124m7.5 10.376h3.375c.621 0 1.125-.504 1.125-1.125V11.25c0-4.46-3.243-8.161-7.5-8.876a9.06 9.06 0 0 0-1.5-.124H9.375c-.621 0-1.125.504-1.125 1.125v3.5m7.5 10.375H9.375a1.125 1.125 0 0 1-1.125-1.125v-9.25m12 6.625v-1.875a3.375 3.375 0 0 0-3.375-3.375h-1.5a1.125 1.125 0 0 1-1.125-1.125v-1.5a3.375 3.375 0 0 0-3.375-3.375H9.75" />
            </svg>
          </button>

          <!-- Tooltip -->
          <span id="tooltip-${index}" class="hidden absolute top-2 left-[50%] -translate-x-1/2 bg-[#3b83f6fb] text-white text-xs py-1 px-2 rounded shadow">
            Link copied!
          </span>
          
        </div>`; 
        });
    } catch (error) {
        // Handle errors (e.g., network issues, response errors)
        console.error("Failed to fetch URL data:", error);
        document.getElementById(destElem_id).innerHTML = "An error occurred while fetching data.";
    } finally {
        // Remove the loading indicator
        document.getElementById(loadingElem_id).innerHTML = "";
    }
}

// Wait until the document is fully loaded before calling the function
document.addEventListener("DOMContentLoaded", function () {
    fetch_url("list", "loading", "url_list"); // Correct destination element IDs
});




// function to copy shortend url
function copyText(uniqueID) {
  const span = document.getElementById(uniqueID);
  const tooltip = document.getElementById(`tooltip-${uniqueID.slice(-1)}`);
  
  if (span) {
      // Copy the text content of the span to the clipboard
      navigator.clipboard.writeText(span.textContent).then(() => {
          // Show tooltip
          tooltip.classList.remove('hidden');
          tooltip.classList.add('flex', 'items-center', 'justify-center');

          // Hide the tooltip after 2 seconds
          setTimeout(() => {
              tooltip.classList.add('hidden');
              tooltip.classList.remove('flex', 'items-center', 'justify-center');
          }, 2000);
      }).catch(err => {
          console.error('Failed to copy text: ', err);
          alert('Failed to copy text.');
      });
  } else {
      console.error('Span element not found.');
  }
}


// Handle Auto pasting in home pages
document.addEventListener("DOMContentLoaded", function () {
    const inputUrl = document.getElementById("input-url");
    const autoPasteToggle = document.getElementById("auto-paste");

    // Load toggle state from localStorage
    const toggleState = localStorage.getItem("autoPasteEnabled");
    if (toggleState === "true") {
        autoPasteToggle.checked = true;
        enableAutoPaste();
    }

    // Add event listener for toggle changes
    autoPasteToggle.addEventListener("change", function () {
        if (autoPasteToggle.checked) {
            enableAutoPaste();
            localStorage.setItem("autoPasteEnabled", "true");
        } else {
            disableAutoPaste();
            localStorage.setItem("autoPasteEnabled", "false");
        }
    });

    function enableAutoPaste() {
        // Automatically paste clipboard content if it's a URL
        navigator.clipboard.readText().then((text) => {
            const urlPattern = /^(https?:\/\/)?([\w-]+\.)+[\w-]+(\/[\w-./?%&=]*)?$/i; // Simple URL regex
            if (urlPattern.test(text.trim())) {
                inputUrl.value = text.trim();
            } else {
                console.warn("Clipboard content is not a valid URL.");
            }
    }).catch((err) => {
        console.error("Failed to read clipboard contents: ", err);
    });
    }

    function disableAutoPaste() {
        console.log("Auto-paste is disabled");
    }
});
