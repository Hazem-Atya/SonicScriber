<template>

    <div class=" container">
                <AudioList  :audios="audios"/>
    </div>
    {{ console.log(audios) }}
</template>    
<script>
import AudioList from './AudioList.vue'
// import AudioDetails from './AudioDetails.vue'
import {API_URL}  from "./common/config.js"


export default {

  mounted() {
    console.log("heeeeeeeeey")
    this.fetchData();
  },
 
  name: 'App',
  components: {
    AudioList,
  },
  data() {
    return {
      audios: []
    };
  },
  methods:{    
    fetchData() {
      fetch(API_URL+'/audios/')
        .then((response) => {
          console.log("hellooooooo")
          response.json().then((data) => {
            console.log(data)
            this.audios = data;
          });
        })
        .catch((err) => {
          console.error(err);
        });
    },
    
  }
}
</script>