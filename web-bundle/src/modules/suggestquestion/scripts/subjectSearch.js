const subjectItems = { 1: 'Mathematik I', 2: 'Mathematik II', 3: 'Materialwissenschaften' };


/*
 * Is triggered when selecting a specific Subject from Search results
 * Updates all UI Elements
 */
function selectSubjectSearchItem(subjectSelectionItem) {
    document.querySelector('#subject-search-mask').value = subjectSelectionItem.getAttribute('data-name');
    document.querySelector('#storage-subject-id').value = subjectSelectionItem.getAttribute('data-id');
    document.querySelector('#button-next-step').classList.remove('disabled');

    document.querySelectorAll('#subject-selection-group, #subject-selection-loader').forEach(function(item) {
        item.classList.add('visually-hidden');
    });
}


/*
 * Show Search Results and handle Loader Icon during request-time
 */
function showSubjectSearchResults() {
    const subjectSelectionLoader = document.querySelector('#subject-selection-loader');
    const subjectSelectionGroup = document.querySelector('#subject-selection-group');

    subjectSelectionGroup.classList.add('visually-hidden');
    subjectSelectionLoader.classList.remove('visually-hidden');

    setTimeout(function() {

        getAndBuildSubjectSearchResults();

        subjectSelectionGroup.classList.remove('visually-hidden');
        subjectSelectionLoader.classList.add('visually-hidden');

    }, 1000);
}


/*
 * Build DOM-Elements for all Searchresult Items
 */
function getAndBuildSubjectSearchResults() {
    // TODO: Implement Ajax Request
    // const searchString = document.querySelector('#subject-search-mask').value;
    const subjectSelectionContainer = document.querySelector('#subject-selection-container');

    subjectSelectionContainer.innerHTML = '';

    for (const [key, value] of Object.entries(subjectItems)) {
        let linkElement = document.createElement('a');
        linkElement.classList.add('list-group-item', 'list-group-item-action', 'subject-selection-item');
        linkElement.setAttribute('data-name', value);
        linkElement.setAttribute('data-id', key);
        linkElement.textContent = value;

        subjectSelectionContainer.appendChild(linkElement);
    }
}




/*
 * EventListener for Triggering Search by Type
 */
document.querySelector('#subject-search-mask').addEventListener('input', function() {

    if(this.value.length >= 3) {
        showSubjectSearchResults();
    }
    else {
        document.querySelector('#subject-selection-group').classList.add('visually-hidden');
    }
});


/*
 * EventListeners for Selecting Subject Item
 */
document.querySelectorAll('.subject-selection-item').forEach(function(item) {
    item.addEventListener('click', function() {
        selectSubjectSearchItem(item);
    });
});
