require("config.options")
require("config.keymaps")
require("config.lazy")

vim.opt.termguicolors = true
vim.opt.background = "dark"

pcall(vim.cmd.colorscheme, "tokyonight")
