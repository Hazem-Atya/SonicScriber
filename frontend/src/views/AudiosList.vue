<template>
    <!-- <img class="background-image" :src="wave" alt="background element" /> -->
    <div class="filter">
        <el-input v-model="searchText" placeholder="Please input" :suffix-icon="Search">
            <template #prepend>Search by name</template>
        </el-input>
        <el-select v-model="selected_filter" placeholder="Filter by type">
            <el-option v-for="item in options" :key="item" :label="item" :value="item" :disabled="item.disabled" />
        </el-select>

    </div>
    <div class="audios-container">
        <AudioCard v-for="audio in filteredAudios" :key="audio.id" :title="audio.name" :description="audio.description"
            :duration="audio.duration" :transcripted="!!audio.user_id" :id="audio.id" :transcription="audio.transcription"/>
    </div>
    <el-skeleton v-if="loading" :rows="10" animated />
</template>
  
<script>
import wave from "../assets/images/wave.png";
import AudioCard from "../components/AudioCard.vue";
import { AudioService } from "../common/audios.service.js"

const options = [
    "All",
    "Transcribed",
    "Not Transcribed",
];

export default {
    name: "AudiosList",
    mounted() {
        this.fetchData();
    },

    components: {
        AudioCard,

    },
    data: function () {
        return {
            selected_filter: "All",
            options,
            wave,
            audios: [],
            searchText: '',
            loading: false

        };
    },
    computed: {
        filteredAudios() {
            if (this.selected_filter == 'All')
                return this.audios.filter(item => {
                    return item.name.trim().toLowerCase().includes(this.searchText.trim().toLowerCase())
                });
            else if (this.selected_filter == 'Transcribed') {
                return this.audios.filter(item => {
                    return item.user_id && item.name.trim().toLowerCase().includes(this.searchText.trim().toLowerCase())
                });
            } else {
                return this.audios.filter(item => {
                    return item.user_id == null && item.name.trim().toLowerCase().includes(this.searchText.trim().toLowerCase())
                })
            }
        },
    },
    methods: {
        fetchData() {
            this.loading = true;
            AudioService.getAllAudios()
                .then((response) => {
                    response.json().then((data) => {
                        this.audios = data.results;
                        this.loading = false;
                    });

                })
                .catch((err) => {
                    console.error(err);
                    this.loading = false;
                });
        },

    },

};
</script>
  
<style>
.el-input-group__prepend {
    background-color: #d4f1f4;
}

.filter {
    margin-bottom: 5vh;
    display: flex;
    gap: 1%;
    width: 96%;
}

.audios-container {
    display: flex;
    row-gap: 5vh;
    column-gap: 1%;
    flex-wrap: wrap;
    position: sticky;
    z-index: 5;
}

.background-image {
    position: absolute;
    width: 70%;
    z-index: 0;
    top: 20vh;
    left: 35vh;
    opacity: 0.8;
}
</style>
  