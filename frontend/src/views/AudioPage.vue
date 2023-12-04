<template>
    <div class="audio-container">

        <audio v-if="!loading" controls>
            <source :src="audio.audio_url" type="audio/mp3" />
            Your browser does not support the audio element.
        </audio>
        <el-skeleton v-if="loading" :rows="5" animated />

        <el-form v-else label-position="top" label-width="100px" :model="formLabelAlign" style="max-width: 1000px"
            class="form">
            <div v-if="audio.user_id">
                {{ audio?.transcription }}
            </div>
            <div v-else>
                <el-form-item>
                    <el-input rows="10" v-model="formLabelAlign.text" type="textarea"
                        placeholder="Write what you are hearing ...." />
                </el-form-item>
                <el-form-item>
                    <el-button @click="submitTranscription">Submit</el-button>
                </el-form-item>
            </div>
        </el-form>
    </div>
</template>
  
<script>
import { reactive } from "vue";
import { ElForm, ElFormItem, ElInput, ElButton } from "element-plus";
import { AudioService } from "../common/audios.service.js"


const formLabelAlign = reactive({
    text: "",
});

export default {
    name: "AudioPage",
    mounted() {
        this.get_audio(this.$route.params.id)
    },

    components: {
        ElForm,
        ElFormItem,
        ElInput,
        ElButton,
    },
    data: function () {
        return {
            formLabelAlign,
            audio: Object,
            loading: Boolean
        };
    },

    methods: {
        get_audio(id) {
            this.loading = true;
            AudioService.getAudioById(id)
                .then((response) => {
                    response.json().then((data) => {
                        this.audio = data;
                        this.loading = false;

                    });
                })
                .catch((err) => {
                    console.error(err);
                });
        },

        submitTranscription() {
            AudioService.submitTranscription(formLabelAlign.text, this.audio.id)
                .then((response) => {
                    response.json().then((data) => {
                        if (!response.ok) {
                    this.$toast.error(JSON.stringify(data), {
                        position: "top-right",
                    });
                } else {
                    this.$toast.success("Transcription submitted successfully!", {
                        position: "top-right",
                    });
                    this.$router.push("/audios")
                }
                    })
                })
        }
    }
};
</script>
  
<style>
.audio-container {
    display: flex;
    align-items: center;
    flex-direction: column;
    gap: 5vh;
}
</style>
  