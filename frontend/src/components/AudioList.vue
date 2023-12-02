<template>



<div class="row">
    <div class="col-6">
        <input placeholder="Search an audio" type="text" class="form-control my-2" >
            <ul class="list-group audios-list">
            <li class="list-group-item active" aria-current="true">An active item</li>
            <li @click="select_audio(audio)" v-for="audio in audios" :key="audio.id" class="list-group-item">{{ audio.name }}</li>
        </ul>
    </div>
    <div v-if="selected_audio" class="col-6">    
       <h1>{{ selected_audio.name  }}</h1>
    <audio  controls>
    <!-- <source src="audio.mp3" type="audio/mp3"> -->
    </audio>
    </div>
</div>




</template>


<script>



export default {

  audios: 'App',
  data() {
    return {
      selected_audio: undefined
    };
  },
  props:{
    audios: Array ,
    msg: String
 },
methods: {
    select_audio(audio) {
     this.selected_audio = audio
    },


}
}

</script>
<style>
.audios-list{
    height: 70vh !important;
    overflow-y: scroll;
    overflow-x: hidden;
}
li{
    cursor: pointer;
}
li:hover{
    background-color: lightgray;
}
</style>