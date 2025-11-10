local builtin = require('telescope.builtin')

-- Find files (by file name)
vim.keymap.set('n', '<leader>ff', builtin.find_files, { desc = 'Telescope find files' })

-- Search file (by content)
vim.keymap.set('n', '<leader>sf', function()
  builtin.grep_string({ search = vim.fn.input("Grep > ") });
end)
