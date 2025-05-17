-- Read the docs: https://www.lunarvim.org/docs/configuration
-- Example configs: https://github.com/LunarVim/starter.lvim
-- Video Tutorials: https://www.youtube.com/watch?v=sFA9kX-Ud_c&list=PLhoH5vyxr6QqGu0i7tt_XoVK9v-KvZ3m6
-- Forum: https://www.reddit.com/r/lunarvim/
-- Discord: https://discord.com/invite/Xb9B4Ny

lvim.leader = "space"

lvim.builtin.which_key.mappings["f"] = {
  name = "File",
  s = { "<Cmd>write<CR>", "Save" },
  f = { function() require('telescope.builtin').find_files() end, "Find file" },
}

lvim.builtin.which_key.mappings["s"] = {
  name = "Search",
  s = {
    function()
      require("telescope.builtin").live_grep({
        additional_args = function()
          return { "--hidden", "--glob", "!.git/" }
        end,
      })
    end,
    "Grep All (incl. hidden)",
  },
}

