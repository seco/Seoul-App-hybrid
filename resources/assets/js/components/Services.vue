<template>
    <v-app>
        <v-toolbar app color="#598bf9">
            <v-layout row wrap>
                <v-flex xs6 style="text-align:left;">
                    <router-link to="/" style="text-decoration: none;">
                        <v-btn icon flat>
                            <v-icon large color="white">arrow_back</v-icon>
                        </v-btn>
                    </router-link>
                </v-flex>
                <v-flex xs6 style="text-align:right; padding-top: 8px; padding-right: 10px;">
                    <h1 style="color: white;">체육시설</h1>
                </v-flex>
            </v-layout>
        </v-toolbar>
        <v-content>
            <v-container style="background-color: #fff;">
                <v-layout wrap align-center>
                    <v-flex xs12>
                        <v-select
                             :items="places"
                             label="- 지역명 -"
                             color="#598bf9"
                             background-color="#aaa"
                             outline
                        ></v-select>
                    </v-flex>
                    <v-flex xs12 style="margin-top: -20px;">
                        <v-select
                            :items="places"
                            label="- 소분류 -"
                            color="#598bf9"
                            background-color="#aaa"
                            outline
                        ></v-select>
                    </v-flex>
                    <v-flex xs12 style="margin-top: -20px;">
                        <v-btn
                            block
                            outline
                            large
                            color="#598bf9"
                        >
                            검색하기
                        </v-btn>
                    </v-flex>
                </v-layout>
            </v-container>
            <v-divider></v-divider>
            <v-container fluid style="padding: 0;">
                <v-layout align-center>
                    <v-flex xs12>
                        <v-list two-line subheader>
                            <v-subheader>
                                서비스 리스트 목록
                            </v-subheader>

                            <v-list-tile>
                                <v-list-tile-content>
                                    <v-list-tile-title>목록1</v-list-tile-title>
                                    <v-list-tile-sub-title>장소1</v-list-tile-sub-title>
                                </v-list-tile-content>
                            </v-list-tile>
                        </v-list>
                    </v-flex>
                </v-layout>
            </v-container>
        </v-content>
    </v-app>
</template>

<script>
    export default {
        name: "ServiceList",
        data: () => ({
            places: [
                '강남구',
                '강동구',
                '강북구',
                '강서구',
                '관악구',
                '광진구',
                '구로구',
                '노원구',
                '도봉구',
                '동대문구',
                '동작구',
                '마포구',
                '서대문구',
                '서초구',
                '성동구',
                '성북구',
                '송파구',
                '양천구',
                '영등포구',
                '용산구',
                '은평구',
                '종로구',
                '중구',
                '중랑구'
            ]
        })
    }
</script>

<style scoped>

</style>