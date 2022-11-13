<template>
<div id="container"> <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 463 316" width="350" height="200" preserveAspectRatio="none">
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
    </svg><br>
    <p>You can catch </p><br>
    <p>the following!</p>
</div>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">  <br><br>
         <div v-for="(g, index) in collections.collections" :key="index">
            <div v-if="(g.season.includes(currentMonth) || g.season == 'All Months') && g.status == 'Not Caught'">
              <div class="card">
                <div :class="'card_img '+g.category"><img :src="require('@/assets/images/'+g.image)"></div>
                  <div class="card_info"><b>{{ g.name }}</b><br> {{ g.location }} <br> {{ g.availability }} 
                    <div class="checkbox-animate">
                      <label>
                        <input type="checkbox" :value="g.id" v-model="collectionIds">
                          <span class="input-check"></span>
                      </label>
                    </div>
                  </div>
              </div>
            </div>
          </div>
      </div>
        <div class="button_container">
                <form @submit.prevent="submitForm">
           <button>Submit</button></form><br>
        </div>
    </div>
  </div>
    </template>

<script>
    import axios from 'axios'

    export default { 
        name: 'ViewCollections',
        data() { 
            return { 
                collections: [],
		currentMonth: [],
                collectionIds: [],
		status: '',
                
            }
        },
        mounted() { 
            this.getCollections()
        },
        methods: { 
            async getCollections() { 
            const CollectionID = this.$route.params.id
                axios
                    .get(`/api/v1/viewcollection/${CollectionID}/`)
                    .then(response => { 
                        this.collections = response.data
                        
			// Get the current month 
			const month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
			const d = new Date();
			const currentMonth = month[d.getMonth()]; 
			this.currentMonth = currentMonth;
                    })
                    .catch(error => { 
                        console.log(error)
                    })


            },
          async submitForm() { 
            const collection = { 
                id: this.collectionIds[0],
		status:  'Caught',
              }
            await axios
             .patch(`/api/v1/collection/${this.collectionIds[0]}/`, collection)
             .then(response => { 
               console.log(response)
               this.$router.push(this.$router.go())})

         }
        }
    }
</script>
