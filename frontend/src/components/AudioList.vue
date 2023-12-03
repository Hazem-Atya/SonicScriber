<template>
  <div class="row">
    <div class="col-6">
      <input v-model="searchText" placeholder="Search an audio" type="text" class="form-control my-2">
      <ul class="list-group audios-list">
        <li @click="select_audio(audio.id)" v-for="audio in filteredAudios" :key="audio.id" class="list-group-item"
          :class="{ 'active': selected_audio?.id == audio.id }">
          {{ audio.name }}
        </li>
      </ul>
    </div>
    <div v-if="selected_audio" class="col-6">
      <h1>{{ selected_audio.name }}</h1>
      <audio ref="player" controls>
        <source v-bind:src="audio_url" type="audio/mp3" />

      </audio>
      <div v-if="selected_audio.transcription">
        {{ selected_audio.transcription }}
      </div>
      <div v-else>
        <textarea v-model="transcription" placeholder="Write your transcription" class="form-control"
          id="exampleFormControlTextarea1" rows="5"></textarea>
        <buttion @click="submitTranscription(transcription, selected_audio.id)" class="btn btn-primary m-2 ">Submit
          transcription</buttion>
      </div>
    </div>
  </div>
</template>


<script >
import { API_URL } from "./common/config.js"



export default {

  audios: 'App',
  data() {
    return {
      selected_audio: undefined,
      audio_url: undefined,
      searchText: ''
    };
  },

  watch: {
    audio_url() {
      this.$refs.player?.load();
    }
  },



  props: {
    audios: Array
  },

  computed: {
    filteredAudios() {
      return this.audios.filter(item =>
        item.name.trim().toLowerCase().includes(this.searchText.trim().toLowerCase())
      );
    },
  },

  methods: {

    select_audio(id) {
      fetch(API_URL + '/audios/' + id)
        .then((response) => {
          response.json().then((data) => {
            console.log(data)
            this.selected_audio = data
            this.audio_url = data.audio_url
          });
        })
        .catch((err) => {
          console.error(err);
        });
    },
    submitTranscription(transcription, audio_id) {
      console.log(transcription)
      console.log(audio_id);
      const requestOptions = {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ transcription: transcription })
      };
      fetch(`${API_URL}/audios/transcribe/${audio_id}`, requestOptions).then((response) => {
        response.json().then((data) => {
          console.log(data)
        })
      })
    }
  }
}

</script>
<style>
.audios-list {
  height: 70vh !important;
  overflow-y: scroll;
  overflow-x: hidden;
}

li {
  cursor: pointer;
}

li:hover {
  background-color: lightgray;
}
</style>