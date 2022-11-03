const projectsCon = document.getElementById('projects')
let data;
const fetchProjects = async () => {
    const response = await fetch("http://127.0.0.1:8000/api/projects/", {
        method: "GET"
    })
    data = await response.json()
    renderProjects()
}

const likeProject = async (id, vote) => {
    const response = await fetch(`http://127.0.0.1:8000/api/projects/${id}/vote/`, {
        method: "POST",
        headers: {
            "Content-type": "Application/json",
            Authorization: "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY3MTU0NTk0LCJpYXQiOjE2NjcxNDg1OTQsImp0aSI6ImMyOTdiNjgzMGZjODQ3ODc4ZTdiMGM4ODljMGIwZjRjIiwidXNlcl9pZCI6NX0.M56b3XBmO74saaJ7ZGQGIbuu7SW8OeK6df2H10S1dP8"
        },
        body: JSON.stringify({
            vote: vote
        })
    })

    const res = await response.json()
    fetchProjects()
    console.log(res)

}


const renderProjects = () => {
    projectsCon.innerHTML = ''
    for (let project of data) {
        // const likes = 
        let likedObj = project.reviews.filter((each) => (
            each.owner.id = project.owner.id
        ))

        let btnValue
        let vote;
        if (likedObj.length > 0) {
            btnValue = likedObj[0].value === 'up' ? 'dislike' : "like"
            vote = likedObj[0].value === 'up' ? 'down' : "up"
        } else {
            btnValue = 'like'
            vote = 'up'
        }
        let projectCon = `
        <div class="column">
        <div class="card project">        
                <img class="project__thumbnail" src="http://127.0.0.1:8000${project.thumbnail}" alt="project thumbnail" />
                <div class="card__body">
                    <h3 class="project__title" style="display:inline">${project.title}</h3>
                    <button class="btn btn--sub" value="up" onclick="likeProject('${project.id}','${vote}')" >${btnValue}</button>
                    <p>
                    <a class="project__author" href="">
                    By ${project.owner.name}
                            </a>
                    </p>
                    <p class="project--rating">
                        <span style="font-weight: bold;">${project.vote_ratio}%</span> Postitive
                        Feedback (${project.vote_total} Votes)
                    </p>
                    <div class="project__tags">
                    
                    </div>
                </div>
        </div>
    </div>

    `

        projectsCon.innerHTML += projectCon
    }
}

fetchProjects()