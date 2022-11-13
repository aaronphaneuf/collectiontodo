<template><div id="container"> <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 463 316" width="350" height="200" preserveAspectRatio="none">
        <defs>
            <filter id="blubby" x="-10%" y="-10%" width="100px" height="100px" filterUnits="objectBoundingBox">
                <feGaussianBlur in="SourceGraphic" result="blur" stdDeviation="20"></feGaussianBlur>
                <feColorMatrix in="blur" mode="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 20 -10"></feColorMatrix>
            </filter>
        </defs>
        <g class="shapes" filter="url(#blubby)">
            <path id="shape1" d="M460.49,106.85c0-82.72-49.8-93.3-81.5-98.11S307.2,2,231.5,2,115.7,3.92,84,8.74.66,24,.66,106.7c0,63.49,6.23,85.09,28.93,102.12C51.14,225,132.91,238.39,231.5,238.39s155.67-5.83,191.77-28.54c33.94-21.35,37.22-36.23,37.22-103Z"></path>
            <path id="shape2" d="M444.05,235.52c0-49-46.24-55.3-75.67-58.15s-66.66-4-136.94-4-107.52,1.14-136.95,4-77.39,9-77.39,58.06c0,37.63,5.79,50.43,26.87,60.53,20,9.58,95.92,17.52,187.47,17.52S376,310,409.49,296.57c31.51-12.65,34.56-21.47,34.56-61Z"></path>
        </g>
    </svg><br><br>
    <p>Who's Playing? </p><br><br>
    <p></p>
</div><br><br>
 

    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
              <div v-for="(g, index) in users" :key="index">
                <a :href="('/collection/'+g.id)"><img class="circular" :src="require('@/assets/images/'+g.id+'.png')"></a> 
              </div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    export default { 
        name: 'ListUser',
        data() { 
            return { 
                users: [],
            }
        },
        mounted() { 
            this.getGame()
        },
        methods: { 
            async getGame() { 
                axios
                    .get('/api/v1/user/')
                    .then(response => { 
                        this.users = response.data
                    })
                    .catch(error => { 
                        console.log(error)
                    })
            },
        }
    }
</script>
