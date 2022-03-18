import { unsplashService } from "@/api";

export const UnsplashAPI = {
  getPhoto: async (search) => {
    try {
      const res = (await unsplashService.get(`${search}`))?.data?.results[0]
        .urls?.regular;
      return res;
    } catch (error) {
      return "https://s3.us-west-2.amazonaws.com/images.unsplash.com/small/photo-1578070181910-f1e514afdd08";
    }
  },
};
