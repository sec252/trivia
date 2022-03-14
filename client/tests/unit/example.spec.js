import { shallowMount } from "@vue/test-utils";
import AdminHome from "@/components/AdminHome.vue";

describe("AdminHome.vue", () => {
  it("renders props.msg when passed", () => {
    const msg = "new message";
    const wrapper = shallowMount(AdminHome, {
      propsData: { msg },
    });
    expect(wrapper.text()).toMatch(msg);
  });
});
