const IuHttpRequest = require('../../../utilities/scripts/IuHttpRequest').IuHttpRequest;

const searchApiMethod = '/subjects/search?query=';

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


    getAndBuildSubjectSearchResults();
    subjectSelectionGroup.classList.remove('visually-hidden');
    subjectSelectionLoader.classList.add('visually-hidden');
    setSelectingSubjectItemEventListeners();
}


/*
 * Build DOM-Elements for all Searchresult Items
 */
getAndBuildSubjectSearchResults = () => {
    const searchString = subjectSearchMask.value;
    const subjectSelectionContainer = document.querySelector('#subject-selection-container');
    const subjectSearchError = document.querySelector('#subject-search-error');

    subjectSelectionContainer.innerHTML = '';
    if(!subjectSearchError.classList.contains('visually-hidden')) {
        subjectSearchError.classList.add('visually-hidden');
    }


    IuHttpRequest.getHttpRequest(searchApiMethod + searchString, (error, requestData) => {
        let searchResult = requestData.subjects;
        if (error !== null || searchResult.length === 0) {
            subjectSearchError.classList.remove('visually-hidden');
        }
        else {
            searchResult.forEach(function(subjectItem) {
                let linkElement = document.createElement('a');
                linkElement.classList.add('list-group-item', 'list-group-item-action', 'subject-selection-item');
                linkElement.href = '#';
                linkElement.setAttribute('data-name', subjectItem.name);
                linkElement.setAttribute('data-id', subjectItem.id);
                linkElement.textContent = subjectItem.name;
        
                subjectSelectionContainer.appendChild(linkElement);
            });
        }
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
