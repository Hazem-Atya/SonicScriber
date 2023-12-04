<template>
    <el-card class="box-card" shadow="always">
        <template #header>
            <div class="card-header">
                <span class="title">{{ title }}</span>
            </div>
        </template>

        <div class="description">{{ description }}</div>
        <div>
            Duration: <span class="title">{{ duration }}s</span>
        </div>
        <router-link :to="'/audio/'+id">
            <div class="footer">
                <el-button v-if="transcripted" circle>
                    <el-icon >
                        <View />
                    </el-icon></el-button>
                <el-button v-else circle>
                    <el-icon >
                        <Edit />
                    </el-icon>
                </el-button>
            </div>
        </router-link>
    </el-card>
</template>

<script>
// eslint-disable-next-line no-unused-vars
import { Edit, View } from "@element-plus/icons-vue";

export default {


    props: {
        title: String,
        description: {
            type: String,
            required: true,
        },
        duration: {
            type: Number,
            required: true,
        },
        transcripted: {
            type: Boolean,
            required: true,
        },
        id: {
            type: Number,
            required: true
        }
    }
};
</script>

<style>
.el-card__header {
    background-color: #8dcaed;
}

.el-card.is-always-shadow {
    box-shadow: 0px 0px 10px 2px #d4f1f4;
}

.card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.title {
    font-size: 14px;
    font-weight: bold;
}

.description {
    margin-bottom: 5px;
}

.box-card {
    width: 240px;
}

.footer {
    margin-top: 1vh;
    display: flex;
    justify-content: flex-end;
}
</style>
