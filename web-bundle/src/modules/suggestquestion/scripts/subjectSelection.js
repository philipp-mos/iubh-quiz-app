// TODO: Will be replaced by API Calls later
const subjectItems = [
    {
        "id": 5,
        "name": "Mathematik I"
    },
    {
        "id": 6,
        "name": "Mathematik II"
    },
    {
        "id": 14,
        "name": "Materialwissenschaften"
    },
];


/*
 * Input Element that captures the Search-String
 */
const subjectSearchMask = document.querySelector('#subject-search-mask');


/*
 * Is triggered when selecting a specific Subject from Search results
 * Updates all UI Elements
 */
selectSubjectSearchItem = (subjectSelectionItem) => {
    subjectSearchMask.value = subjectSelectionItem.getAttribute('data-name');
    document.querySelector('#storage-subject-id').value = subjectSelectionItem.getAttribute('data-id');
    document.querySelector('#button-next-step').classList.remove('disabled');

    document.querySelectorAll('#subject-selection-group, #subject-selection-loader').forEach(function(item) {
        item.classList.add('visually-hidden');
    });
}


/*
 * Show Search Results and handle Loader Icon during request-time
 */
showSubjectSearchResults = () => {
    const subjectSelectionLoader = document.querySelector('#subject-selection-loader');
    const subjectSelectionGroup = document.querySelector('#subject-selection-group');

    subjectSelectionGroup.classList.add('visually-hidden');
    subjectSelectionLoader.classList.remove('visually-hidden');

    setTimeout(function() {

        getAndBuildSubjectSearchResults();
        subjectSelectionGroup.classList.remove('visually-hidden');
        subjectSelectionLoader.classList.add('visually-hidden');
        setSelectingSubjectItemEventListeners();

    }, 1000);
}


/*
 * Build DOM-Elements for all Searchresult Items
 */
getAndBuildSubjectSearchResults = () => {
    // TODO: Implement Ajax Request
    // const searchString = subjectSearchMask.value;
    const subjectSelectionContainer = document.querySelector('#subject-selection-container');

    subjectSelectionContainer.innerHTML = '';

    subjectItems.forEach(function(subjectItem) {
        let linkElement = document.createElement('a');
        linkElement.classList.add('list-group-item', 'list-group-item-action', 'subject-selection-item');
        linkElement.href = '#';
        linkElement.setAttribute('data-name', subjectItem.name);
        linkElement.setAttribute('data-id', subjectItem.id);
        linkElement.textContent = subjectItem.name;

        subjectSelectionContainer.appendChild(linkElement);
    });
}


/*
 * EventListeners for Selecting Subject Item
 */
setSelectingSubjectItemEventListeners = () => {
    document.querySelectorAll('.subject-selection-item').forEach(function(item) {
        item.addEventListener('click', function() {
            selectSubjectSearchItem(item);
        });
    });
}


/*
 * EventListener for Triggering Search by Type
 */
if(subjectSearchMask) {
    subjectSearchMask.addEventListener('input', function() {

        if(this.value.length >= 3) {
            showSubjectSearchResults();
        }
        else {
            document.querySelector('#subject-selection-group').classList.add('visually-hidden');
        }
    });
}
